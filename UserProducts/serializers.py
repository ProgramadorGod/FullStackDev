from rest_framework import serializers
from .models import ProductRelation
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse




class UserProductSerializer(serializers.ModelSerializer):
    
    
    class Meta: 
        model = ProductRelation
        fields = '__all__'

from rest_framework.decorators import api_view

@api_view(['GET'])
@csrf_exempt  
def FilterByUser(request):
    user = request.user
    user_products = ProductRelation.objects.filter(user=user)
    serializer = UserProductSerializer(user_products, many=True)
    return JsonResponse({'data': serializer.data})





