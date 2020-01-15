from rest_framework import serializers
from .models import Peliculas_Populares

class Peliculas_Populares_Serializers(serializers.ModelSerializer):

    class Meta:
        model = Peliculas_Populares
        fields = '__all__'

