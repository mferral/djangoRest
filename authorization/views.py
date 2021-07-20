from django.shortcuts import render
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
# Create your views here.
class AuthToken(ObtainAuthToken):            
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']                                            
        token, created = Token.objects.get_or_create(user=user)
        print (user)
        return Response({
            'token': token.key,
            'full_name': user.get_full_name()
        })

class RemoveToken(APIView):
    def post(self, request):
        request.user.auth_token.delete()
        return Response(status =status.HTTP_200_OK)
