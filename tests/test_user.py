# def f():
#     return 3


# def test_function():
#     assert f() == 3
from main.models import CustomUser
from django.test import TestCase, RequestFactory
from main.views import UserViewSet

def test_user():
    user = CustomUser(password="123456",first_name="john", last_name="doe", email="johndoe@blah.com", language='1234', region='NA')
    assert str(user.email) == "johndoe@blah.com"
    assert str(user.language) == '1234'
    assert str(user.password) == '123456'
    assert str(user.first_name) == 'john'
    assert str(user.last_name) == 'doe'
    assert str(user.region) == 'NA'

def test_user_request(rf):
    user = CustomUser(password="123456",first_name="john", last_name="doe", email="johndoe@blah.com", language='1234', region='NA')
    request = rf.get(path=f'/v1/users/', body={ "email": user.email, "password": user.password})
    response = UserViewSet.find_user_by_email(email, request)
