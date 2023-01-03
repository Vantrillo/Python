from django.shortcuts import render
import urllib.request
import json
from datetime import datetime

def index(request):
    if request.method=='POST':
        city = request.POST['city'].replace(" ", "+")
        api_key = '151e7769c7e71055034b26d42c93846c'
        source = urllib.request.urlopen(f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid={api_key}').read()
        list_data = json.loads(source)
        data = {
            'city': request.POST['city'].title(),
            'country': f"{list_data['sys']['country']}",
            'coord': f'({list_data["coord"]["lat"]}, {list_data["coord"]["lon"]})',
            'dt': datetime.fromtimestamp(list_data['dt']),
            'temp': f'{list_data["main"]["temp"]} °F',
            'pressure': f'{list_data["main"]["pressure"]}',
            'humidity': f'{list_data["main"]["humidity"]}',
            'main': f'{list_data["weather"][0]["main"]}',
            'desciption': f'{list_data["weather"][0]["description"]}',
            'icon': list_data["weather"][0]["icon"],
        }
    else:
        data = {}
    return render(request, 'weather/index.html', data)