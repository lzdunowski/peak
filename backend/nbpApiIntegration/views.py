from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.template import loader

import requests

# Helper function for getting Gold price
# def make_get_request(url):
#   response = requests.get(url)
#   return response

# Prev version of index with Gold price
# def index(request):
#     url = "http://api.nbp.pl/api/cenyzlota?format=json"
#     response = make_get_request(url)

#     if response.status_code == 200:
#         json = response.json()
#     else:
#         json = f"Request failed with status code {response.status_code}"
    
#     return HttpResponse(json[0]['data'])

from .models import Currency

def index(request):
    currencies_list = Currency.objects.all()
    template = loader.get_template("nbpApiIntegration/index.html")
    context = {
        "currencies_list": currencies_list,
    }
    return render(request, "nbpApiIntegration/index.html", context)

def detail(request, currency_id):
    currency = get_object_or_404(Currency, pk=currency_id)
    return render(request, "nbpApiIntegration/detail.html", {"currency": currency})
