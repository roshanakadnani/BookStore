from django.contrib import admin
from .models import Book, Author, Rating, Stock


class BookAdmin(admin.ModelAdmin):
    pass


class AuthorAdmin(admin.ModelAdmin):
    pass


class RatingAdmin(admin.ModelAdmin):
    pass


class StockAdmin(admin.ModelAdmin):
    pass


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Rating, RatingAdmin)
admin.site.register(Stock, StockAdmin)
