from django.shortcuts import render
from rest_framework import viewsets
from .models import Peliculas_Populares
from .serializers import Peliculas_Populares_Serializers

# Create your views here.
class Peliculas_Populares_ViewSet(viewsets.ModelViewSet):
    serializer_class = Peliculas_Populares_Serializers
    queryset = Peliculas_Populares.objects.all()
