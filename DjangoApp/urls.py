"""
URL configuration for DjangoApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Api.views import ItemViewSet
from django.conf.urls.static import static
from django.conf import settings
from StoreApp.views import Store
from contact import views

router = DefaultRouter()
router.register(r'items', ItemViewSet, basename='item')


router.register(r'products', Store, basename='product')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html')),
    path('About', TemplateView.as_view(template_name='index.html')),
    path('Contact', TemplateView.as_view(template_name='index.html')),
    path('Cart', TemplateView.as_view(template_name='index.html')),
    path('Store', TemplateView.as_view(template_name='index.html')),
    path('api/', include(router.urls)),
    path('FormUrl/', views.ContactView, name="FormUrl")
    


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.MEDIA_URL2, document_root=settings.MEDIA_ROOT2)