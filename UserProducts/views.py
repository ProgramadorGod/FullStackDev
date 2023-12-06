from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json
from rest_framework import viewsets
from UserProducts.models import ProductRelation
from StoreApp.models import Product
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .serializers import UserProductSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
# Create your views here.

class UserProducts(viewsets.ModelViewSet):
    queryset=ProductRelation.objects.all()
    serializer_class= UserProductSerializer
    #permission_classes = (IsAuthenticated,)

    # def list(self, request) -> (Response):
    #     return Response(self.get_serializer(self.get_queryset().filter(user=request.user), many=True).data)

@csrf_exempt  
@require_POST
def AddProduct(request):
    
    if request.method == 'POST':
        data = json.loads(request.body)
        productId= data.get("productId")
        action = data.get("action")
        user = authenticate(request, username="Lol", password="passwordgod")
        
        login(request,user)
        print(request.user)
        print("Login Success...")

        print(request.user.is_authenticated)
        if action == "Add_Product":
            
            print("Action passed")
            try:
                if request.user.is_authenticated:
                    print("GOD")
                    productt = Product.objects.get(id=productId)
                    print(productt.Name)
                    print("Request USER : " + str(request.user))
                    ProductRelation.objects.create(
                    user = request.user,
                    product = productt,
                    )
                    return JsonResponse({'Status': 'Ok'})
                else:
                    pass
            except Exception as e:
                pass



    return JsonResponse({'Status': 'Ok'})




from django.shortcuts import render
from StoreApp.models import Product
from rest_framework import viewsets
from .serializers import UserProductSerializer
# Create your views here.


class Lol(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class  = UserProductSerializer

