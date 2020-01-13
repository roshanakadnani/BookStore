from rest_framework import serializers, generics
from .models import Book, Stock, Rating
from rest_framework import viewsets
from django.contrib.auth.models import User
import json
from django.db import models
from rest_framework.views import APIView
from rest_framework.response import Response
from . import auth
from .serializers import BookSerialiser, RateSerialiser, StockSerialiser


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerialiser


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

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class RateViewSet(viewsets.ModelViewSet):
    authentication_classes = [auth.RestAuth]
    queryset = Rating.objects.all()
    serializer_class = RateSerialiser

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class StockViewSet(viewsets.ModelViewSet):
    authentication_classes = [auth.RestAuth]
    queryset = Stock.objects.all()
    serializer_class = StockSerialiser

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [auth.RestAuth]
    queryset = Book.objects.all()
    serializer_class = BookSerialiser


class Book(APIView):
    authentication_classes = [auth.RestAuth]

    def post(self, request):
        x = BookViewSet.filter_queryset(request, request.data)
        return self.process_request(request, request.data)

    def get(self, request, format=None):
        x = BookViewSet.filter_queryset(request, request.data)
        if not (x is None):
            return self.request.query_params.f(request, request.query_params)
