from django.shortcuts import render,redirect
from django.views import View
from Restaurant.models import *
# Create your views here.
from django.conf import settings
from django.core.mail import send_mail
import random
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.decorators import login_required
    



def send_email_to_client(email,name,Rest_name):
    subject = "We Got Your Request"
    message = f'''We Got Your Request!
Hi,{name} we recieve Your request For parter with us(Become a Foody partner today)
We Review Your Restaurant {Rest_name} within 24hrs and contact You
Have a nice day!!!







Thank You
Team Foody
    '''
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    return send_mail(subject,message,from_email,recipient_list,fail_silently=False)


def send_email_for_password(email,password):
    subject = "Login Details"
    message = f'''

This is your login UserName & password

Your Username : {email}
Your Password : {password}


Login to proccess Your application



Thank You
Team Foody
    '''
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]

    return send_mail(subject,message,from_email,recipient_list,fail_silently=False)

class Register_Restaurant(View):
    def get(self,request):
        '''
        Rest_name = models.CharField(max_length=50)
    Owner_name = models.CharField(max_length=50)
    Email = models.EmailField()
    Owner_contact = models.BigIntegerField()
    Rest_location = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
'''
        return render(request,'Register_Restaurant.html')
    
    def post(self,request):
        Rest_name = request.POST.get('Restaurant_name')
        Owner_name = request.POST.get('Owner_name')
        Email = request.POST.get('email')
        Owner_contact = request.POST.get('Contact')
        Rest_location = request.POST.get('Rest_loc')

        obj = Rest_details.objects.create(
            Rest_name=Rest_name,
            Owner_name=Owner_name,
            Email=Email,
            Owner_contact=Owner_contact,
            Rest_location=Rest_location
                          )
        obj.save()
        send_email_to_client(Email,Owner_name,Rest_name)
        password = ''
        for i in range(0,8):
            num = random.randint(0,9)
            password += str(num)
        rest_login = Login_details.objects.create(
            username=Email,
            password=password
        )
        rest_login.save()

        send_email_for_password(Email,password)

        return render(request,'Register_Restaurant.html')
    

class Rest_login(View):
    def get(self,request):
        return render(request,'Rest_login.html')

    def post(self,request):
        
        username = request.POST.get('rusername')
        password = request.POST.get('rpassword')
        
        user = authenticate(request,username=username,password=password)
        
        if not User.objects.filter(username=user).exists():
            messages.info(request,f'UserName Not Exits')
            return redirect('User_Login')

        elif user is None:
            messages.info(request,f'Invalid Password Or UserName')
            return redirect('User_Login')
            
        else:
            login(request,user)
            
            #data = Rest_details.objects.filter(Email='bhoirraj872@gmail.com')
            #return render(request,'Restaurant_main.html',{'data':data})
            #return redirect('Restaurant_main')
    
            return redirect('Restaurant_main')

        
        
        return render(request,'Rest_login.html')
    

class Rest_home(View):


    def get(self,request):
        foods = Menu.objects.all()
        

        return render(request,'Restaurant_main.html',{"Foods":foods}    )
        
    
    def post(self,request):
        #current_user = request.user
        data = Rest_details.objects.filter(Email = 'bhoirraj872@gmail.com')
        Rest_name1 = data[0].Rest_name
        print(Rest_name1)
        Menu_name = request.POST.get("Food_Name")
        Menu_desc = request.POST.get("Food_Desc")
        Menu_Price = request.POST.get("Food_Price")
        Menu_img = request.FILES.get("Food_Img")
        obj = Menu.objects.all()
        obj = Menu.objects.create(
           
            Menu_name=Menu_name,
            Menu_desc=Menu_desc,
            Menu_Price=Menu_Price,
            Menu_img=Menu_img
        )
        obj.save()
        return redirect('Restaurant_main')

        

        
        return render(request,'Restaurant_main.html')
    
@login_required(login_url=Rest_login)
def Add_Food(request):
    return render(request,'Add Menu.html')