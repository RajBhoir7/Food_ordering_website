from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
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
    