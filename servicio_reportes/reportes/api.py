from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from reportes.models import Torneo
from reportes.serializers import torneo_serializer
from django.http import JsonResponse
import datetime

@api_view(['GET'])
def torneo_api_view(request):
    if request.method == 'GET':
        torneos = Torneo.objects.all()
        t_serializer = torneo_serializer(torneos, many=True)
        return Response(t_serializer.data)

@api_view(['GET'])
def torneo_esp_api_view(request,id_t):  #Prueba de consulta por atributo ide
    if request.method == 'GET':
        torneo = Torneo.objects.filter(ide=id_t)
        t_serializer = torneo_serializer(torneo)
        return Response(t_serializer.data)


@api_view(['GET'])
def torneos_fechas_api_view(request): #Prueba de consulta por fechas
    if request.method == 'GET':
        fecha_inicio = request.GET.get('fecha_inicio')
        fecha_final = request.GET.get('fecha_final')
        if fecha_inicio and fecha_final:
            torneos = Torneo.objects.filter(fecha_inicio__range=[fecha_inicio, fecha_final]).values()
            return JsonResponse({'torneos': list(torneos)})
        else:
            return JsonResponse({'error': 'Los parametros fecha de inicio y final son requeridos.'})