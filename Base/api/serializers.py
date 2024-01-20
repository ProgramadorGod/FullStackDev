from rest_framework.serializers import ModelSerializer
from Base.models import UserProducts

class UserProductsSerializer(ModelSerializer):
    class Meta:
        model = UserProducts
        fields = '__all__'