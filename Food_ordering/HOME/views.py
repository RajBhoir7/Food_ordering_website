from django.shortcuts import render
from Restaurant.models import Rest_details
#import requests
# Create your views here.
import json
def home(request):  
    #ip = requests.get("https://api.ipify.org?format=json")
    #ip_data = json.loads(ip.text)
    #res = requests.get('http://ip-api.com/json/'+ip_data['ip'])
    #location_data_one = res.text
    #location_data = json.loads(location_data_one)

                                        #,{'data':location_data}

    hotels_in_user_location = Rest_details.objects.all()
    return render(request,'home.html',{'data':hotels_in_user_location})

#http://ip-api.com/json/24.48.0.1?fields=message,country,countryCode,region,regionName,city,district,zip,lat,lon,#timezone,isp,org,as,query


#res = requests.get('http://ip-api.com/json/'+ip_data['ip']+'/fields=message,country,countryCode,region,#regionName,city,district,zip,lat,lon,timezone,isp,org,as,query')
    