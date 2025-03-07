Basic Weather Forecast app using OpenWeatherAPI

How to use the app:
1. create a new virtual environment:
```python3-venv -m venv .venv ```
2. activate the environment:
``` source .venv/bin/activate ```
3. clone the repository:
``` git clone '' ```
4. change directory:
``` cd WeatherForecast ```
5. install requirements:
``` pip install -r requirements.txt ```
6. create the .env file:
``` cp .env.copy .env ```
7. enter your OpenWeatherAPI key in the .env file:
``` API_KEY="your-api-key" ```
8. run the app
``` python manage.py runserver ```