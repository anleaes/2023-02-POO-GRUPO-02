from django.shortcuts import render
from .models import Material_Used
from rest_framework import viewsets
from .serializer import Material_UsedSerializer

# Após o comentario "# Create your views here."

class Material_UsedViewSet(viewsets.ModelViewSet):
    queryset = Material_Used.objects.all()
    serializer_class = Material_UsedSerializer
