from rest_framework import serializers

from .models import *
class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaModel
        fields = '__all__'

class DocesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoceModel
        fields = '__all__'


