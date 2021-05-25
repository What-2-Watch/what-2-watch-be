import pytest
from main.models import CustomUser
from django.test import TestCase

def test_user():
    user = CustomUser(password="123456",first_name="john", last_name="doe", email="johndoe@blah.com", language='1234', region='NA')
    assert str(user.email) == "johndoe@blah.com"
    assert str(user.language) == '1234'
    assert str(user.password) == '123456'
    assert str(user.first_name) == 'john'
    assert str(user.last_name) == 'doe'
    assert str(user.region) == 'NA'
