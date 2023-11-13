# serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = "__all__"  # Ajusta según tus necesidades
