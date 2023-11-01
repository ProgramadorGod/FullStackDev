from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to='itemspics', null=True, blank=True)

    def __str__(self) -> str:
        return self.name