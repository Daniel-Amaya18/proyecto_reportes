from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from rest_framework.response import Response
import requests
import json

# Create your views here.
def torneos(request):
    response = requests.get('https://jsonplaceholder.typicode.com/users').text
    # torneo = response.json()
    torneo = json.loads(response)
    print(torneo)
    print(type(torneo))
    return Response(torneo)