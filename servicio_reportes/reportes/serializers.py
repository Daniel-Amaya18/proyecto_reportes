from rest_framework import serializers
from .models import Torneo

class torneo_serializer(serializers.ModelSerializer):
    class Meta:
        model = Torneo
        fields = ['ide','person_1','person_2','person_3'] # Modificar atributos