from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import MyTokenObtainView
from rest_framework.routers import DefaultRouter
from .views import getUserProducts


router= DefaultRouter()
router.register(r'UserProducts', getUserProducts, basename='UserProducts')


urlpatterns = [
    path('',include(router.urls)),
    path('', views.getRoutes),
    path('token/', MyTokenObtainView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]