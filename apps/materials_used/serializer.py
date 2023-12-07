from .models import Material_Used
from rest_framework import serializers

class Material_UsedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material_Used
        fields = '__all__'