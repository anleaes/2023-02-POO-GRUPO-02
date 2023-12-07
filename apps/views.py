from django.shortcuts import render
from .models import Location
from rest_framework import viewsets
from .serializer import LocationSerializer

# Após o comentario "# Create your views here." e crie as views "Category".

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer 
