from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from main.models import CustomUser

class CustomUserBackend(ModelBackend):

    def authenticate(self. request, **kwargs):
        email = kwargs['email']
        password = kwargs['password']
        try:
            user = CustomUser.objects.get(email=email)
            if user.user.check_password(password) is True:
                return user.user
        except  CustomUser.DoesNotExist:
            pass
