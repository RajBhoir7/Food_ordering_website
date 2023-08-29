from django.shortcuts import render,HttpResponse

# Create your views here.

def Register_Restaurant(request):
    return render(request,'Register_Restaurant.html')
