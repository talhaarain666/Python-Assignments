import requests
from pprint import pprint

# API_KEY = '6cdc48bcbbb397eb71b7a8ae074cf64a' #My API key
API_KEY = 'cb771e45ac79a4e8e2205c0ce66ff633'
city = input("Enter the city name: ")

base_url = f"http://api.openweathermap.org/data/2.5/weather?appid={API_KEY}&q={city}"

weather_data = requests.get(base_url).json()

pprint(weather_data)