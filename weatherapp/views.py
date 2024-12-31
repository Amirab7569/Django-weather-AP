from django.shortcuts import render
import requests
import datetime

# Create your views here.
def index(request):
    if 'city' in request.POST:
        city=request.POST['city']
    else:
        city='tehran'
    url='https://api.openweathermap.org/data/2.5/weather'
    params={'q':city,'units':'metric','appid':'f0e9fec1f7ab1854bf9653ef58c178a5'}
    result=requests.get(url=url,params=params).json()
    description= result['weather'][0]['description']
    temp= result['main']['temp']
    icon= result['weather'][0]['icon']
    day=datetime.date.today()
    return render(request,'weatherapp/index.html',{'description':description,'temp':temp,'icon':icon,'day':day,'city':city})