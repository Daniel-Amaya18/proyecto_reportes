from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.http import HttpResponse
import datetime
import requests
import json

# Create your views here.
@api_view(['GET', 'POST'])
def torneo(request,id_t):  #Prueba de consulta por atributo ide
    if request.method == 'GET':
        response = requests.get("https://jsonplaceholder.typicode.com/users") # Cambiar url
        return JsonResponse(response.json(), safe=False)
    elif request.method == 'POST':
        response = requests.get("https://jsonplaceholder.typicode.com/users") # Cambiar url
        return JsonResponse(response.json(), safe=False)


@api_view(['GET', 'POST'])
def torneos_fechas_api_view(request): #Prueba de consulta por fechas
    if request.method == 'GET':
        fecha_inicio = request.GET.get('fecha_inicio')
        fecha_final = request.GET.get('fecha_final')
        if fecha_inicio and fecha_final:
            torneos = Torneo.objects.filter(fecha_inicio__range=[fecha_inicio, fecha_final]).values()
            return JsonResponse({'torneos': list(torneos)})
    elif request.method == 'POST':
        fecha_inicio = request.GET.get('fecha_inicio')
        fecha_final = request.GET.get('fecha_final')
        if fecha_inicio and fecha_final:
            torneos = Torneo.objects.filter(fecha_inicio__range=[fecha_inicio, fecha_final]).values()
            return JsonResponse({'torneos': list(torneos)})
    else:
        return JsonResponse({'error': 'Los parametros fecha de inicio y final son requeridos.'})
