from .models import Supervisor
from rest_framework import serializers

class SupervisorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supervisor
        fields = '__all__'
        
    