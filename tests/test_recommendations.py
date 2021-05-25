import pytest
from main.models import Subscription, CustomUser, Watchlist, Thumb
from django.test import TestCase, Client
from recommendations import views

class RecommendationTestCast(TestCase):
  def test_recommendations(self):
    user = CustomUser(password="123456", first_name="john", last_name="doe",
                    email="johndoe@blah.com", language='1234', region='NA')
    user.save()
    netflix = Subscription(user=user, name="netflix", api_provider_id=8)
    netflix.save()
    amazon_prime = Subscription(user=user, name="Amazon Prime", api_provider_id=9)
    amazon_prime.save()
    disney_plus = Subscription(user=user, name="Disney+", api_provider_id=337)
    disney_plus.save()
    itunes = Subscription(user=user, name="Itunes", api_provider_id=2)
    itunes.save()
    c = Client()
    response = c.get(f"/v1/movies?user={user.id}")
    self.assertEqual(len(response.json()['results']), 20)
    self.assertEqual(type(response.json()['results'][0]['title']), str)
    self.assertEqual(type(response.json()['results'][0]['title']), str)
    self.assertEqual(type(response.json()['results'][0]['genre_ids']), list)
    self.assertEqual(type(response.json()['results'][0]['genre_ids'][0]), int)
    self.assertEqual(type(response.json()['results'][0]['id']), int)
    self.assertEqual(type(response.json()['results'][0]['genre_ids'][0]), int)
    self.assertEqual(type(response.json()['results'][0]['poster_path']), str)
    self.assertEqual(type(response.json()['results'][0]['backdrop_path']), str)
    self.assertEqual(type(response.json()['results'][0]['release_date']), str)
    self.assertEqual(type(response.json()['results'][0]['vote_average']), float)

  def test_genre_recommendations(self):
    user = CustomUser(password="123456", first_name="john", last_name="doe",
                      email="johndoe@blah.com", language='1234', region='NA')
    user.save()
    netflix = Subscription(user_id=user.id, name="netflix", api_provider_id=8)
    netflix.save()
    amazon_prime = Subscription(user_id=user.id, name="Amazon Prime", api_provider_id=9)
    amazon_prime.save()
    disney_plus = Subscription(user_id=user.id, name="Disney+", api_provider_id=337)
    disney_plus.save()
    itunes = Subscription(user_id=user.id, name="Itunes", api_provider_id=2)
    itunes.save()
    thumb = Thumb(title='The Great Escape', api_movie_id=2, api_genre_id=341, up=True, user=user)
    thumb.save()
    thumb2=Thumb(title='James Bond', api_movie_id=3, api_genre_id=341, up=True, user=user)
    thumb2.save()
    thumb3=Thumb(title='The Red House', api_movie_id=4, api_genre_id=489, up=True, user=user)
    thumb3.save()
    thumb4 = Thumb(title='Gladiator', api_movie_id=5, api_genre_id=489, up=True, user=user)
    thumb4.save()
    thumb5 = Thumb(title='House', api_movie_id=6, api_genre_id=341, up=True, user=user)
    thumb5.save()
    self.assertEqual(views.recommendations_by_genre(user), 341)
  
