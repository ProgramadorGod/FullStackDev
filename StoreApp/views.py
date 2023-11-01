from django.shortcuts import render
from StoreApp.models import Product
from rest_framework import viewsets
from .serializers import ProductSerializer
# Create your views here.


class Store(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class  = ProductSerializer