from django.shortcuts import render
from .models import Contribuitor
from rest_framework import viewsets
from .serializer import ContribuitorSerializer

# Após o comentario "# Create your views here." e crie as views "Category".

class ContribuitorViewSet(viewsets.ModelViewSet):
    queryset = Contribuitor.objects.all()
    serializer_class = ContribuitorSerializer
