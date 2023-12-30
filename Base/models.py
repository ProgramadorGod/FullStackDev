from django.db import models
from django.contrib.auth.models import User
from StoreApp.models import Product
# Create your models here.
class UserProducts(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product,null="True",on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)



