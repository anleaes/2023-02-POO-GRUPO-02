from .models import Entity
from rest_framework import serializers

class EntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entity
        fields = '__all__'
        
        