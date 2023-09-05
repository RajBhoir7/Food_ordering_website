from django.shortcuts import render
from django.views import View
from Restaurant.models import Rest_details
# Create your views here.


class Cart(View):
    def get(self,request):
        hotels_in_user_location = Rest_details.objects.all()
        return render(request,'Cart_Page.html',{'data':hotels_in_user_location})