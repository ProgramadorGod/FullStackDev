from django.db import models
# models.py

from django.contrib.auth.models import User

class Usuario(models.Model):
    # Puedes agregar campos adicionales específicos de tu aplicación si es necesario
    usuario_django = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.usuario_django.username
    
