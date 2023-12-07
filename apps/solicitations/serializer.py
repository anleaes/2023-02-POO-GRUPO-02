from .models import Solicitation
from rest_framework import serializers


class SoliciationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solicitation
        fields = '__all__'


# Para chamar somentes os atributos de interesse:
        # fields = ['id','created_on', 'updated_on', 'name', 'description']