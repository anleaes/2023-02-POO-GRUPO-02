from django.shortcuts import render
from .models import Solicitation
from rest_framework import viewsets
from .serializer import SoliciationSerializer

# Após o comentario "# Create your views here." e crie as views "Category".

class SolicitationViewSet(viewsets.ModelViewSet):
    queryset = Solicitation.objects.all()
    serializer_class = SoliciationSerializer
