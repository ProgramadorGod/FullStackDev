from django.conf import settings
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet
from django.conf.urls.static import static


router = DefaultRouter()
router.register(r'items', ItemViewSet, basename='item')

urlpatterns = [
    path('api/', include(router.urls)),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)