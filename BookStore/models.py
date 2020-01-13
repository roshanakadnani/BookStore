from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models


class Author(models.Model):
    """Model class for authors"""

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.first_name) + " " + str(self.last_name)


class Book(models.Model):
    """Model class for books"""

    title = models.CharField(max_length=150)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    price = models.IntegerField(null=True)

    def __str__(self):
        return self.title


class Stock(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.ForeignKey(Author, on_delete=models.CASCADE)


class Rating(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    time = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # ratings go from 1-5
    rating = models.IntegerField(
        choices=(
            (1, '1'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
            (5, '5'),
        )
    )
