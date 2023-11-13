from django.shortcuts import render

# Create your views here.
# views.py
from rest_framework import generics, viewsets
from django.contrib.auth.models import User
from .models import Usuario
from .serializer import UsuarioSerializer

class UsuarioLista(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer




