from django.db import models

# Create your models here.



class Product(models.Model):
    Name = models.CharField(max_length=200)
    Price = models.FloatField(max_length=28)
    Image = models.ImageField(upload_to='storepics', null=True, blank=True)

    def __str__(self) -> str:
        return self.Name
