from django.shortcuts import render
from .models import Material
from rest_framework import viewsets
from .serializer import MaterialSerializer

# Após o comentario "# Create your views here." e crie as views "Category".

class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer  
