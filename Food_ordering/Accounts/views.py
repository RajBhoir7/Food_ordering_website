from django.shortcuts import render,redirect
from django.contrib import messages
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
# Create your views here.


class User_Register(View):
    def get(self,request):
        return render(request,'User_Register.html')


    def post(self,request):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('email')
        password1 = request.POST.get('password1')
        
        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            username=username,
            
        )
        user.set_password(password1)
        user.save()
    
        return render(request,'User_Register.html')
    
class User_Login(View):
    def get(self,request):
        return render(request,'Login_page.html')
    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if not User.objects.filter(username=username).exists():
            messages.info(request,f'UserName Not Exits')
            return redirect('User_Login')

        elif user is None:
            messages.info(request,f'Invalid Password Or UserName')
            return redirect('User_Login')
            
        else:
            login(request,user)
            return redirect('home')
        return render(request,'Login_page.html')
        

class User_logout(View):
        
        def get(self,request):
            logout(request)        
            return redirect('User_Login')

        
    