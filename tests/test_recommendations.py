import pytest
from main.models import Subscription, CustomUser, Watchlist, Thumb
from django.test import TestCase, Client
from recommendations import views

class RecommendationTestCast(TestCase):
  def test_recommendations(self):
    user = CustomUser(password="123456", first_name="john", last_name="doe",
                    email="johndoe@blah.com", language='1234', region='NA')
    user.save()
    netflix = Subscription(user_id=user.id, name="netflix", api_provider_id=8)
    amazon_prime = Subscription(user_id=user.id, name="Amazon Prime", api_provider_id=9)
    disney_plus = Subscription(user_id=user.id, name="Disney+", api_provider_id=337)
    itunes = Subscription(user_id=user.id, name="Itunes", api_provider_id=2)
    c = Client()
    response = c.get(f"/v1/movies?user={user.id}")
    self.assertEqual(len(response.json()['results']), 20)
  
