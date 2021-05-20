from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
import requests
import environ
from environ import Env

env = environ.Env()
environ.Env.read_env()
# Create your views here.
@api_view(['GET'])
@renderer_classes((JSONRenderer,))
def get_movies(request):
    url = "https://api.themoviedb.org/3/discover/movie"
    params = {"api_key": env('API_KEY'), "language": "en-US", "sort_by": "popularity.desc", "include_adult": "false", "include_video": "false", "page": "1", "with_watch_providers": "2|8", "watch_region": "US"}
    response = requests.get(url, params=params)
    movies = response.json()
    return Response(movies, status=status.HTTP_200_OK)
