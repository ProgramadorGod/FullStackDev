from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json
from django.core.mail import EmailMessage



# Create your views here.

@csrf_exempt  
@require_POST
def ContactView(request):
    data = json.loads(request.body.decode('utf-8'))
    Name = data["name"]
    Email = data["email"]
    Phone = data["phone"]
    Message = data["message"]

    print('Datos recibidos en Django:', data)
    Phone = Phone + Name
    email = EmailMessage(Phone, Message, "pipenet12@gmail.com",[Email])
    email.send()

    return JsonResponse({'Status': 'Ok'})