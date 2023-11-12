from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):

    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     representation["categirt¡¡¡"] = ({
    #         "name": "Luizzz",
    #         "type": "pendejo"
    #     })
    #     return representation

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'password')
