from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.contrib.auth.models import AbstractUser
from main.managers import CustomUserManager

class CustomUser(AbstractUser):
    pass
    username = None
    email = models.EmailField(max_length=100, unique=True, null=False, blank=False)
    # subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    language = models.CharField(max_length=5, null=False, blank=False, default=0)
    region = models.CharField(max_length=5, null=False, blank=False, default=0)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Subscription(models.Model):
    user = models.ForeignKey(CustomUser, related_name='subscriptions', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    api_provider_id = models.PositiveIntegerField()

    def __str__(self):
        return self.name
