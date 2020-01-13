from django.urls import path, include
from BookStore.book_api import BookViewSet, RateViewSet, StockViewSet
from BookStore.book_api import UserLogin, UserInfoView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'rates', RateViewSet)
router.register(r'stocks', StockViewSet)

urlpatterns = [
    path('user/login/', UserLogin.as_view()),
    path('user/info/', UserInfoView.as_view()),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
