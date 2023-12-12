from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from  rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import UserProductsSerializer
from Base.models import UserProducts

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['name'] = user.username
        token['email'] = user.email
        return token
    
class MyTokenObtainView(TokenObtainPairView):
    serializer_class=MyTokenObtainPairSerializer

@permission_classes([IsAuthenticated])
class getUserProducts(viewsets.ModelViewSet):
    serializer_class = UserProductsSerializer
    def get_queryset(self):
        user=self.request.user
        return UserProducts.objects.filter(user=user)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getNotes2(request):
    user = request.user
    notes=user.note_set.all()
    serializer = UserProductsSerializer(UserProducts,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/token',
        '/api/token/refresh',
    ]
    return Response(routes)