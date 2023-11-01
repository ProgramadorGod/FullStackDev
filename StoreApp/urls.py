from django.conf import settings
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import Store
from django.conf.urls.static import static


router2 = DefaultRouter()
router2.register(r'Products', Store, basename='product')

urlpatterns = [
    path('api/', include(router2.urls)),

]