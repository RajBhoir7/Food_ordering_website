from django.shortcuts import render
from django.views import View
# Create your views here.


class User_Register(View): 

    def get(self,request):
        return render(request,'User_Register.html')
    
class User_Login(View):
    def get(self,request):
        return render(request,'Login_page.html')