from django.shortcuts import render,redirect
from django.views import View
from Restaurant.models import *
# Create your views here.
from django.conf import settings
from django.core.mail import send_mail
import random
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout

        
    



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


        x = Login_details.objects.filter(username=username)
        p = Login_details.objects.filter(password=password)


        user = authenticate(username=x,password=p)
        print(user,username,password)

        if not Login_details.objects.filter(username=username).exists():
            messages.info(request,f'UserName Not Exits')
            return redirect('Rest_login')

        elif user is None:
            messages.info(request,f'Invalid Password Or UserName')
            return redirect('Rest_login')
            
        else:
            login(request,user)
            return redirect('home')

        
        
        return render(request,'Rest_login.html')