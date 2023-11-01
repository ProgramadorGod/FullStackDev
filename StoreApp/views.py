from django.shortcuts import render
from StoreApp.models import Product
from rest_framework import viewsets
from .models import Item

# Create your views here.


class Store(viewsets.ModelViewSet):
    Procuts = Product.objects.all()
