from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from profiles_api import serializers


class HelloAppView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """return list of APIView"""
        an_apiview = [
            'Uses HTTP method as function (get, post,..)',
            'similar to django view',
            'control over app layer',
            'mapped to URL',
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})

    def post(self, request):
        """hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """handle updating an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, ph=None):
        """ partial update to object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, ph=None):
        """ delete object"""
        return Response({'method': 'DELETE'})

class HelloViewSet(viewsets.ViewSet):
    """Test API viewset"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """return a message"""

        a_viewset = [
            'uses actions (list, create, retrieve)',
            'maps to routers',
            'provides more functions',
        ]

        return Response({'message': 'Hello', 'a_viewset': a_viewset})

    def create(self, request):
        """create message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    def retrieve(self, request, pk=None):
        """getting object by ID"""
        return Response({'http_method': 'GET'})
    def update(self, request, pk=None):
        """update object"""
        return Response({'http_method': 'PUT'})
    def partial_update(self, request, pk=None):
        """partial update object"""
        return Response({'http_method': 'PATCH'})
    def destroy(self, request, pk=None):
        """delete object"""
        return Response({'http_method': 'DELETE'})
