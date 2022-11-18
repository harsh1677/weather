from django.shortcuts import render

# Create your views here.
import requests

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=eca7e4f5bd469a3a70ed160491aea84b'
    city = 'Pune'



    city_weather = requests.get(url.format(city)).json()
    print (city_weather)
    weather = {
        'city' : city,
        'temperature' : city_weather['main']['temp'],
        'description' : city_weather['weather'][0]['description'],
        'icon' : city_weather['weather'][0]['icon'],
        'humidity':city_weather['main']['humidity'],
        'feels':city_weather['main']['feels_like']
    }
    return render(request, 'index.html', {'weather':weather})