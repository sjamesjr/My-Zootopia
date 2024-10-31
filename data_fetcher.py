import requests
import os
from dotenv import load_dotenv
import json

load_dotenv()
API_KEY = os.getenv('API_KEY')


def fetch_data(animal_name):
    URL = "https://api.api-ninjas.com/v1/animals"
    params = {"name": animal_name}
    header = {"X-Api-Key": API_KEY}
    response = requests.get(URL, params=params, headers=header)
    return response.json()
