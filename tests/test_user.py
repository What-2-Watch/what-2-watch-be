# def f():
#     return 3


# def test_function():
#     assert f() == 3
from main.models import CustomUser
from main.models import Subscription
from django.test import TestCase

def test_user():
    user = CustomUser(password="123456",first_name="john", last_name="doe", email="johndoe@blah.com", language='1234', region='NA')
    assert str(user.email) == "johndoe@blah.com"
    assert str(user.language) == '1234'
    assert str(user.password) == '123456'
    assert str(user.first_name) == 'john'
    assert str(user.last_name) == 'doe'
    assert str(user.region) == 'NA'

def test_subscription():
    user = CustomUser(password="123456",first_name="john", last_name="doe", email="johndoe@blah.com", language='1234', region='NA')

    sub = user.subscription_set.create(name="netflux", api_provider_id=8)
    breakpoint()
