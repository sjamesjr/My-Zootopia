import requests
import os
from dotenv import load_dotenv
import json

# Load environment variables from a .env file
load_dotenv()
API_KEY = os.getenv('API_KEY')


def fetch_data(animal_name):
    """Fetches data for a specified animal from the API Ninjas Animals API.

    Sends a GET request to the API with the animal name as a parameter and
    retrieves the data in JSON format.

    Args:
        animal_name (str): The name of the animal to fetch data for.

    Returns:
        dict or list: The JSON response from the API containing animal data.
                      Returns an empty dictionary if the request fails.
    """
    # Define the API endpoint and parameters
    URL = "https://api.api-ninjas.com/v1/animals"
    params = {"name": animal_name}
    header = {"X-Api-Key": API_KEY}

    # Send a GET request to the API
    response = requests.get(URL, params=params, headers=header)

    # Return JSON data from response
    return response.json()

