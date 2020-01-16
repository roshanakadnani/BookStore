from django.http import Http404
from rest_framework import serializers, generics, status
from .models import Book, Stock, Rating
from rest_framework import viewsets
from django.contrib.auth.models import User
import json
from django.db import models
from rest_framework.views import APIView
from rest_framework.response import Response
from . import auth
from .serializers import BookSerialiser, RateSerialiser, StockSerialiser


class UserInfoView(APIView):
    authentication_classes = [auth.RestAuth]

    def get(self, request):
        user = request.user
        return Response({
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
        })


class UserLogin(APIView):
    def post(self, request):

        user = User.objects.filter(models.Q(username=request.data['username'])).first()
        if not user:
            return Response({
                'errors': 'Invalid credentials',
            })

        if not user.is_active or not user.check_password(request.data['password']):
            return Response({
                'errors': 'Invalid credentials',
            })

        token = auth.encode_user(user).decode('utf-8')
        return Response({
            'token': token,
        })


"""class NewBook(APIView):
    authentication_classes = [auth.RestAuth]

    def post(self, request):
        print(request.data)
        return Response({
            'status': 'book created',
        })
"""


class BookViewSet(viewsets.ModelViewSet):
    authentication_classes = [auth.RestAuth]
    queryset = Book.objects.all()
    serializer_class = BookSerialiser

    
class RateViewSet(viewsets.ModelViewSet):
    authentication_classes = [auth.RestAuth]
    queryset = Rating.objects.all()
    serializer_class = RateSerialiser


class StockViewSet(viewsets.ModelViewSet):
    authentication_classes = [auth.RestAuth]
    queryset = Stock.objects.all()
    serializer_class = StockSerialiser

    
class StockDetail(APIView):
    authentication_classes = [auth.RestAuth]
    
    def get_object(self, pk):
        try:
            return Stock.objects.get(pk=pk)
        except Stock.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = StockSerialiser(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = StockSerialiser(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response({"message": "Stock with id `{}` has been deleted.".format(pk)},status=204)


class BookDetail(APIView):
    authentication_classes = [auth.RestAuth]

    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = BookSerialiser(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = BookSerialiser(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response({"message": "Book with id `{}` has been deleted.".format(pk)},status=204)


class RatingDetail(APIView):
    authentication_classes = [auth.RestAuth]

    def get_object(self, pk):
        try:
            return Rating.objects.get(pk=pk)
        except Rating.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = RatingDetail(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = RatingDetail(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response({"message": "Rate with id `{}` has been deleted.".format(pk)},status=204)
