# def f():
#     return 3


# def test_function():
#     assert f() == 3
import pytest
from main.models import CustomUser
from main.models import Subscription
from django.test import TestCase
@pytest.mark.django_db
@pytest.fixture(autouse=True)
def enable_db_access_for_all_tests(db):
    pass

def test_user():
    user = CustomUser(password="123456",first_name="john", last_name="doe", email="johndoe@blah.com", language='1234', region='NA')
    assert str(user.email) == "johndoe@blah.com"
    assert str(user.language) == '1234'
    assert str(user.password) == '123456'
    assert str(user.first_name) == 'john'
    assert str(user.last_name) == 'doe'
    assert str(user.region) == 'NA'

class SubscriptionTestCase(TestCase):
    def test_subscription(self):
        user = CustomUser(password="123456",first_name="john", last_name="doe", email="johndoe@blah.com", language='1234', region='NA')
        user.save()
        sub = Subscription(user_id=user.id, name="netflux", api_provider_id=8)
        sub2 = Subscription(user_id=user.id, name="prime", api_provider_id=9)
        sub3 = Subscription(user_id=user.id, name="Banana", api_provider_id=10)
        sub.save()
        sub2.save()
        sub3.save()
        # user.save()
        record = Subscription.objects.get(id=1)
        breakpoint()
        self.assertEqual(record.user.first_name, "john")

# user.subscription_set.all().first()
# this is how you access user subscriptions might want to look into reverse relationship?
# https://stackoverflow.com/questions/17328910/django-what-is-reverse-relationship
    # assert user.subscriptions.count() == 1

    # assert user.subscriptions.count 1
    # breakpoint()
