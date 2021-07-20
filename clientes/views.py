from django.shortcuts import render
from rest_framework import generics
from .models import Cliente
from .serializers import ClienteSerializer, ClientePostSerializer, ClientePutSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from authorization.authentication import ExpiringTokenAuthentication
from authorization.mispermisos import Permiso
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class ClienteList(generics.ListAPIView):
    pagination_class = None
    serializer_class = ClienteSerializer

    def get_queryset(self):        
        queryset = Cliente.objects.all()
        return queryset

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def list_clientes(request):

    if (not Permiso.is_valid(request.user, 'clientes.view_cliente')):
        return Response(status=status.HTTP_400_BAD_REQUEST)

    snippets = Cliente.objects.all()
    serializer = ClienteSerializer(snippets, many=True)    
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_cliente(request):
    serializer = ClientePostSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_cliente(request, pk):
    try:
        snippet = Cliente.objects.get(pk=pk)
    except Cliente.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ClientePutSerializer(snippet, data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)