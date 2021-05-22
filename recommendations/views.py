from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
import requests
import environ
from environ import Env
from main.models import CustomUser, Thumb
from django.db.models import Count

env = environ.Env()
environ.Env.read_env()
# Create your views here.

def recommendations_by_genre(user):
    count = user.thumbs.values_list('api_genre_id').annotate(genre_count=Count('api_genre_id')).order_by('-genre_count')
    return count[0][0]

def user_subscriptions(user):
    provider_ids = user.subscriptions.values_list('api_provider_id', flat=True)
    content = []
    for id in provider_ids:
        content.append(str(id))
    pipe_separated = "|".join(content)
    return pipe_separated

@api_view(['GET'])
@renderer_classes((JSONRenderer,))
def get_movies(request):
    user_id = request.GET.get('user')
    user = CustomUser.objects.get(pk=user_id)
    url = "https://api.themoviedb.org/3/discover/movie"
    language = user.language
    region = user.region
    watch_providers = user_subscriptions(user)
    genre = recommendations_by_genre(user)
    params = {"api_key": env('API_KEY'), "language": language, "sort_by": "popularity.desc", "include_adult": "false", "include_video": "false", "page": "1", "with_watch_providers": watch_providers, "watch_region": region, "with_genres": genre}
    response = requests.get(url, params=params)
    movies = response.json()
    return Response(movies, status=status.HTTP_200_OK)
