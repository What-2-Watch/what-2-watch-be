from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from main.models import CustomUser
from main.serializers import UserSerializer
from rest_framework.decorators import api_view, action
from rest_framework import viewsets
from main.models import CustomUser

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def find_user_by_email(self, request, email):
        breakpoint()
    # @api_view(['GET', 'PUT', 'DELETE'])
    # def user_detail(request, pk):
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
        #     return Response(serializer.data)
        #
        # elif request.method == 'PUT':
        #     serializer = UserSerializer(user, data=request.data)
        #     if serializer.is_valid():
        #         serializer.save()
        #         return Response(serializer.data)
        #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        #
        # elif request.method == 'DELETE':
        #     user.delete()
        #     return Response(status=status.HTTP_204_NO_CONTENT)
