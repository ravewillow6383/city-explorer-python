from os import environ
import json
import requests

class Location:
    def __init__(self, search_query, info):
        self.search_query = search_query
        self.formatted_query = info['formatted_address']
        self.latitude = info['geometry']['location']['lat']
        self.longitude = info['geometry']['location']['lng']

    def serialize(self):
        return vars(self)
    
@staticmethod
def fetch(query):
    """
    fetches geocode data for given location;
    returns as json
    """

    api_key = environ.get('GEOCODE_API_KEY')

    url = f'https://maps.googleapis.com/maps/api/geocode/json?address={query}&key={api_key}'

#    use request library to return data back in variable
    locations = requests.get(url).json()

    location = Location(query, locations['results'][0])
    
    return json.dumps(location.serialize())