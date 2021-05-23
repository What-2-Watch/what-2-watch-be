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
import random

env = environ.Env()
environ.Env.read_env()
# Create your views here.

def recommendations_by_genre(user):
    count = user.thumbs.filter(up=True).values_list('api_genre_id').annotate(genre_count=Count('api_genre_id')).order_by('-genre_count')
    if count[0][1] >= 3:
        return count[0][0]
    else:
        return ''


def recommendations_by_actor(user):
    count = user.thumbs.filter(up=True).values_list('api_actor_id').annotate(
        actor_count=Count('api_actor_id')).order_by('-actor_count')
    if count[0][1] >= 3:
        return count[0][0]
    else:
        return ''


def recommendations_by_director(user):
    count = user.thumbs.filter(up=True).values_list('api_director_id').annotate(
        director_count=Count('api_director_id')).order_by('-director_count')
    if count[0][1] >= 3:
        return count[0][0]
    else:
        return ''

def user_subscriptions(user):
    provider_ids = user.subscriptions.values_list('api_provider_id', flat=True)
    content = []
    for id in provider_ids:
        content.append(str(id))
    pipe_separated = "|".join(content)
    return pipe_separated

def recommendations_by_genre_actor(user):
    return {"api_key": env('API_KEY'), "language": user.language, "sort_by": "popularity.desc", "include_adult": "false", "include_video": "false",
            "page": "1", "with_watch_providers": user_subscriptions(user), "watch_region": user.region, "with_genre": recommendations_by_genre(user), "with_cast": recommendations_by_actor(user)}


def recommendations_by_genre_director(user):
    return {"api_key": env('API_KEY'), "language": user.language, "sort_by": "popularity.desc", "include_adult": "false", "include_video": "false",
            "page": "1", "with_watch_providers": user_subscriptions(user), "watch_region": user.region, "with_genre": recommendations_by_genre(user), "with_crew": recommendations_by_director(user)}


def recommendations_by_actor_director(user):
    return {"api_key": env('API_KEY'), "language": user.language, "sort_by": "popularity.desc", "include_adult": "false", "include_video": "false",
     "page": "1", "with_watch_providers": user_subscriptions(user), "watch_region": user.region, "with_cast": recommendations_by_actor(user), "with_crew": recommendations_by_director(user)}

def determine_params(user):
    if user.thumbs.count() >= 10:
        random_recommendation = [recommendations_by_genre_actor(user), recommendations_by_genre_director(user), recommendations_by_actor_director(user)]
        return random.choice(random_recommendation)
    else:
        return {"api_key": env('API_KEY'), "language": user.language, "sort_by": "popularity.desc", "include_adult": "false", "include_video": "false", "page": "1", "with_watch_providers": user_subscriptions(user), "watch_region": user.region}

def remove_thumbs_down(user, movies):
    thumbs_down = user.thumbs.filter(up=False).values_list('api_movie_id', flat=True)
    content = []
    movie_list = movies['results']
    for id in thumbs_down:
        content.append(id)
    good_movies = []
    for movie in movie_list:
        if movie['id'] in content:
            continue
        else:
            good_movies.append(movie)
    return good_movies

@api_view(['GET'])
@renderer_classes((JSONRenderer,))
def get_movies(request):
    user = CustomUser.objects.get(pk=request.GET.get('user'))
    params = determine_params(user)
    response = requests.get("https://api.themoviedb.org/3/discover/movie", params=params)
    movies = response.json()
    good_movies = {'results': remove_thumbs_down(user, movies)}
    return Response(good_movies, status=status.HTTP_200_OK)
