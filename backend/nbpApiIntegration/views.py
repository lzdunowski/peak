from django.shortcuts import render
from django.http import HttpResponse

import requests

def make_get_request(url):
  response = requests.get(url)
  return response

def index(request):
    url = "http://api.nbp.pl/api/cenyzlota?format=json"
    response = make_get_request(url)

    if response.status_code == 200:
        json = response.json()
    else:
        json = f"Request failed with status code {response.status_code}"
    
    return HttpResponse(json[0]['data'])
