from .models import Contribuitor
from rest_framework import serializers

class ContribuitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contribuitor
        fields = '__all__'
        
        # Para chamar todos os atributos:
        # fields = '__all__'
        
        # Para chamar somentes os atributos de interesse:
        # fields = ['id','created_on', 'updated_on', 'name', 'description']