import requests
import json
def fetch_data(animal_name):
    URL = "https://api.api-ninjas.com/v1/animals"
    params = {"name": {animal_name}}
    API_KEY = {"X-Api-Key": "L/K6XFChAP081dYR34/DsA==49HJZUygpquvzVDn"}
    response = requests.get(URL, params=params, headers=API_KEY)
    return response.json()
