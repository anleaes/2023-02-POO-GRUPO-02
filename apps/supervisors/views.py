from django.shortcuts import render
from .models import Supervisor
from rest_framework import viewsets
from .serializer import SupervisorSerializer

# Após o comentario "# Create your views here." e crie as views "Supervisor".

class SupervisorViewSet(viewsets.ModelViewSet):
    queryset = Supervisor.objects.all()
    serializer_class = SupervisorSerializer  
