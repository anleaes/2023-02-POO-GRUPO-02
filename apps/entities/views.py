from django.shortcuts import render
from .models import Entity
from rest_framework import viewsets
from .serializer import EntitySerializer

# Após o comentario "# Create your views here." e crie as views "Category".

class EntityViewSet(viewsets.ModelViewSet):
    queryset = Entity.objects.all()
    serializer_class = EntitySerializer  