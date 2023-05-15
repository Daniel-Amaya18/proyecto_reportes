from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.http import HttpResponse
from django.template import Template, Context
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

### View de test
def test_id(request):
    return render(request,'reportes/torneo_por_id.html')

def test_aux(request):
    if request.method == 'POST':
        # Obtener los valores del formulario
        id = request.POST.get('id_torneo')

        # Redireccionar a otra vista
        return redirect('torneo_test_id', id_t=id)
    
    return render(request, 'reportes/torneo_por_id.html')

def torneo_test_id(request, id_t):
    # Lógica de la vista nueva
    response = requests.get("https://jsonplaceholder.typicode.com/users") # Cambiar url
    return JsonResponse(response.json(), safe=False)

def test_fecha(request):
    return render(request,'reportes/torneo_por_fecha.html')

def test_fecha_aux(request):
    if request.method == 'POST':
        # Obtener los valores del formulario
        fecha_inicio = request.POST.get('fecha_inicio')
        fecha_fin = request.POST.get('fecha_fin')

        # Redireccionar a otra vista
        return redirect('torneo_test_fecha', fecha_inicial=fecha_inicio, fecha_final=fecha_fin)
    
    return render(request, 'reportes/torneo_por_fecha.html')

def torneo_test_fecha(request, fecha_inicial, fecha_final):
    # Lógica de la vista nueva
    response = requests.get("https://jsonplaceholder.typicode.com/users") # Cambiar url
    return JsonResponse(response.json(), safe=False)
