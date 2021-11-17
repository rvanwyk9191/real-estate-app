from django.http import HttpResponse
import requests
from . import mappers
from aws import secretmanager

def getSaleListings(request, city, state):
    url = "https://realty-mole-property-api.p.rapidapi.com/saleListings"
    lowerCity = city.lower()
    querystring = {"city": lowerCity.capitalize(), "state": mappers.convertState(state)}

    headers = {
        'x-rapidapi-host': "realty-mole-property-api.p.rapidapi.com",
        'x-rapidapi-key': secretmanager.getSecretFrom('RABID_API')
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    if (response.text == "[]"):
        return HttpResponse("Sorry, no results found!!")
    return HttpResponse(response.text)

def getNearestTrainStations(request, lat, long):
    google_api_key = secretmanager.getSecretFrom('GOOGLE_API')

    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=" + lat + "%2C" + long + "&radius=3000&type=station&keyword=train&key=" + google_api_key

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    return HttpResponse(response.text)
