import pytest
from main.models import Subscription, CustomUser
from django.test import TestCase

class SubscriptionTestCase(TestCase):
    def test_subscription(self):
        user = CustomUser(password="123456", first_name="john", last_name="doe",
                          email="johndoe@blah.com", language='1234', region='NA')
        user.save()
        sub = Subscription(user_id=user.id, name="netflux", api_provider_id=8)
        sub2 = Subscription(user_id=user.id, name="prime", api_provider_id=9)
        sub3 = Subscription(user_id=user.id, name="Banana", api_provider_id=10)
        sub.save()
        sub2.save()
        sub3.save()
        self.assertEqual(sub.user.first_name, "john")
        self.assertEqual(sub.name, "netflux")
        self.assertEqual(sub.user_id, 1)
        self.assertEqual(sub.api_provider_id, 8)
        self.assertEqual(sub2.name, "prime")
        self.assertEqual(sub2.user_id, 1)
        self.assertEqual(sub2.api_provider_id, 9)
        self.assertEqual(sub3.name, "Banana")
        self.assertEqual(sub3.user_id, 1)
        self.assertEqual(sub3.api_provider_id, 10)
        self.assertEqual(len(user.subscriptions.all()), 3)
