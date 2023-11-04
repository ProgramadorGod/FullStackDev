from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json


# Create your views here.

@csrf_exempt  
@require_POST
def ContactView(request):
    data = json.loads(request.body.decode('utf-8'))
    
    print('Datos recibidos en Django:', data)

    

    return JsonResponse({'Status': 'Ok'})