from django.db import models

# Create your models here.
class Peliculas_Populares (models.Model):

    portada = models.CharField(max_length=400)
    titulo = models.CharField(max_length=90)
    creador = models.CharField(max_length=90)
    puntaje = models.IntegerField()
    genero = models.CharField(max_length=50)
    hora = models.IntegerField()
    minutos = models.IntegerField()
    descripcion = models.CharField(max_length=700)

    def __str__(self):
            return self.titulo


    

   
