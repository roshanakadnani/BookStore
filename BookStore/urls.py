from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

from BookStore.book_api import BookViewSet, RateViewSet, StockViewSet, BookDetail, StockDetail, RatingDetail
from BookStore.book_api import UserLogin, UserInfoView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'ratings', RateViewSet)
router.register(r'stocks', StockViewSet)

urlpatterns = [
    path('user/login/', UserLogin.as_view()),
    path('user/info/', UserInfoView.as_view()),
    path('', include(router.urls)),
    path('books/<int:pk>/', BookDetail.as_view()),
    path('ratings/<int:pk>/', RatingDetail.as_view()),
    path('stocks/<int:pk>/', StockDetail.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns = format_suffix_patterns(urlpatterns)
