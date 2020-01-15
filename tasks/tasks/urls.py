from django.contrib import admin
from django.urls import path

from rest_framework.routers import DefaultRouter
from Peliculas.views import Peliculas_Populares_ViewSet

router = DefaultRouter()
router.register(r'Peliculas', Peliculas_Populares_ViewSet)

urlpatterns = router.urls 

urlpatterns  += [
    path('admin/', admin.site.urls),
]
