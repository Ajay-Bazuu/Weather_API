from django.shortcuts import render
import requests
from django.contrib import messages
from datetime import datetime

# Create your views here.
def index(request):
    api_key='02bf860a6ea350c1248e35a8b98bb59c'
    if 'city' in request.POST:
        city=request.POST['city']
    else:
        city='kathmandu'
    url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    param={'units':'metric'}
    try:

        data=requests.get(url,param).json() # changes to dictionary
        temp=data['main']['temp']
        desc=data['weather'][0]['description']
        icon=data['weather'][0]['icon']
        wind_speed=data['wind']['speed']
        hum=data['main']['humidity']
        date=datetime.now()
        return render(request, 'index.html',{"temp":temp,'city':city,'desc':desc,'icon':icon,'wind_speed':wind_speed,'hum':hum,'date':date})
    except:
        city="Unknown"
        data=requests.get(url,param).json() # changes to dictionary
        temp=0
        desc="There is no such City Registered "
        icon="Unkonwn"
        wind_speed=0        
        hum=0
        messages.error(request," Unable to find City ")
        return render(request, 'index.html',{"temp":temp,'city':city,'desc':desc,'icon':icon,'wind_speed':wind_speed,'hum':hum})