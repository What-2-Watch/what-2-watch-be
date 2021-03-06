"""what2watch URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from main.models import CustomUser
from django.urls import include, path
from rest_framework import routers
from main import views
from recommendations.views import get_movies
from rest_framework.versioning import URLPathVersioning

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'subscriptions', views.SubscriptionViewSet)
router.register(r'watchlists', views.WatchlistViewSet)
router.register(r'thumbs', views.ThumbViewSet)
# router.register(r'subscriptions', views.SubscriptionViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
# urlpatterns = [
#     path('', include(router.urls)),
#     path('admin/', admin.] #

urlpatterns = [
    path(r'v1/', include(router.urls)),
    path(r'v1/admin/', admin.site.urls),
    path(r'v1/movies', get_movies, name = 'get_movies'),
    path(r'v1/rest-auth/', include('rest_auth.urls')),
]
