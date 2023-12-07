from django.shortcuts import render
from .models import Rating
from rest_framework import viewsets
from .serializer import RatingSerializer

# Após o comentario "# Create your views here." 

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer 
