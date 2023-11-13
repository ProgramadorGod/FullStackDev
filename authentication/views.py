from django.shortcuts import redirect, render
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm
from django.http.response import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password
from django.contrib.auth import login
from .forms import CustomUserCreationForm



# Create your views here.
class VRegister(View):
    def get(self, request):
        form = CustomUserCreationForm()

        return render(request,'authentication/register.html', {'form':form})
    
    def post(self,request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('/')
        else:
            return redirect('authentication/Register/')





class Login(View):
    def get(self, request):
        print(request.user)
        return render(request,'authentication/login.html')
        #form = UserCreationForm()
        #return render(request,'authentication/register.html', {"form":form})

    def post(self, request):
        user_name = request.POST.get("user")
        password = request.POST.get("password")
        user = User.objects.filter(username=user_name).first()

        if user:
            if check_password(password, user.password):
                authenticated_user = authenticate(request,username=user_name,password=password)
                if authenticated_user is not None:
                    login(request, authenticated_user)  # Establece la sesión de usuario

                    return redirect("/")
                
            return HttpResponse("Invalid password.")

        return HttpResponse("User not found")