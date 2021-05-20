from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, action
from rest_framework import viewsets
from main.models import CustomUser, Subscription, Watchlist, Thumb
from main.serializers import UserSerializer, SubscriptionSerializer, WatchlistSerializer, ThumbSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    # @api_view(['GET', 'PUT', 'DELETE'])
    # def user_detail(request, pk=0):
        # """
        # Retrieve, update or delete a user.
        # """
        # try:
        #     user = CustomUser.objects.get(pk=pk)
        # except CustomUser.DoesNotExist:
        #     return Response(status=status.HTTP_404_NOT_FOUND)
        #
        # if request.method == 'GET':
        #     serializer = UserSerializer(user)
        #     queryset = CustomUser.objects.all()
        # elif request.method == 'POST':
        #     serializer = UserSerializer(user, data=request.data)
        #     if serializer.is_valid():
        #         serializer.save()
        #         return JsonResponse(serializer.data, status=201)
        #     return JsonResponse(serializer.errors, status=400)
        #     if serializer.is_valid():
        #         serializer.save()
        #         return Response(serializer.data)
        #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        #
        # elif request.method == 'DELETE':
        #     user.delete()
        #     return Response(status=status.HTTP_204_NO_CONTENT)


class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)


class WatchlistViewSet(viewsets.ModelViewSet):
    queryset = Watchlist.objects.all()
    serializer_class = WatchlistSerializer


class ThumbViewSet(viewsets.ModelViewSet):
    queryset = Thumb.objects.all()
    serializer_class = ThumbSerializer
