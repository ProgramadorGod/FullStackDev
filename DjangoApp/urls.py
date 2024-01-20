
from django.contrib import admin
#from rest_framework_jwt.views import obtain_jwt_token
from django.urls import path
from django.views.generic import TemplateView
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Api.views import ItemViewSet
from django.conf.urls.static import static
from django.conf import settings
from StoreApp.views import Store
from contact.views import ContactView
from Base.api import views
#from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from Base.api.views import getUserProducts
from Base.api.views import getNotes2


router = DefaultRouter()
router.register(r'items', ItemViewSet, basename='item')
router.register(r'products', Store, basename='product')
router.register(r'UserProducts', getUserProducts, basename="UserProducts")


urlpatterns = [
    # url(r'^api-token-auth/', obtain_jwt_token),
    path('admin/', admin.site.urls),
    
    path('', TemplateView.as_view(template_name='index.html')),
    path('About', TemplateView.as_view(template_name='index.html')),
    path('Contact', TemplateView.as_view(template_name='index.html')),
    path('Cart', TemplateView.as_view(template_name='index.html')),
    path('Store', TemplateView.as_view(template_name='index.html')),
    path('api/', include(router.urls)),
    path('api2/', include('Base.api.urls')),
    path('FormUrl/', ContactView, name="FormUrl"),
    path('authentication/', include('authentication.urls')),
    path('notes2/', views.getNotes2),


#    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),



]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.MEDIA_URL2, document_root=settings.MEDIA_ROOT2)