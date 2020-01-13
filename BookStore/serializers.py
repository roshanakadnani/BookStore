from rest_framework import serializers

from BookStore.models import Book, Stock, Rating


class BookSerialiser(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'price')


class StockSerialiser(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stock
        fields = ('id', 'book', 'quantity')


class RateSerialiser(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'book', 'time', 'user', 'rating')
