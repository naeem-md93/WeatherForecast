import os

from django.shortcuts import render

import requests
import dotenv

dotenv.load_dotenv()


def render_index_page(request, message: str = None, result: dict[str, str] = None):

    context = {}
    if message is not None:
        context['message'] = message

    if result is not None:
        context['result'] = result

    return render(request,'index.html', context=context)


def index(request):

    API_ENDPOINT = os.getenv("ENDPOINT", "https://api.openweathermap.org/data/2.5/weather")
    API_KEY = os.getenv("API_KEY", "")

    message = None
    result = None

    if API_KEY == "":
        message = 'Please add your `WeatherAPI` API key into the "API_KEY" variable within the `.env` file'
        return render_index_page(request, message, result)

    if request.method == 'POST':
        city = request.POST.get('city').lower()

        if len(city) < 3:
            message = 'Please enter valid city name ...!'
            return render_index_page(request, message, result)

        response = requests.get(f"{API_ENDPOINT}?q={city}&appid={API_KEY}")

        if response.status_code == 200:
            data = response.json()
            result = {
                "coord_lon": data['coord']['lon'],
                "coord_lat": data['coord']['lat'],
                "weather": data['weather'][0]['description'],
                "base": data['base'],
                "main_temp": data['main']['temp'],
                "main_feels_like": data['main']['feels_like'],
                "main_temp_min": data['main']['temp_min'],
                "main_temp_max": data['main']['temp_max'],
                "main_pressure": data['main']['pressure'],
                "main_humidity": data['main']['humidity'],
                "main_sea_level": data['main']['sea_level'],
                "main_grnd_level": data['main']['grnd_level'],
                "visibility": data['visibility'],
                "wind_speed": data['wind']['speed'],
                "wind_deg": data['wind']['deg'],
                "clouds_all": data['clouds']['all'],
                "dt": data['dt'],
                "sys_country": data['sys']['country'],
                "sys_sunrise": data['sys']['sunrise'],
                "sys_sunset": data['sys']['sunset'],
                "timezone": data['timezone'],
                "name": data['name'],
            }
            return render_index_page(request, result=result)
        if response.status_code != 200:
            return render_index_page(request, message=response.json()["message"])

    return render_index_page(request, message, result)
