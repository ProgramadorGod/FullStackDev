from rest_framework import serializers
from .models import ProductRelation

class UserProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductRelation
        fields = '__all__'