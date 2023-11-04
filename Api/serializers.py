from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):

    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     representation["categirt¡¡¡"] = ({
    #         "name": "Luizzz",
    #         "type": "pendejo"
    #     })
    #     return representation

    class Meta:
        model = Item
        fields = '__all__'