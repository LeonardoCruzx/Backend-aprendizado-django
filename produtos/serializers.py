from rest_framework import serializers

from .models import *
class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaModel
        fields = '__all__'

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProdutoModel
        fields = '__all__'

    def to_representation(self, instance):
        representation = super(ProdutoSerializer, self).to_representation(instance)
        try:
            representation['product_picture'] = instance.product_picture.url
        except:
            representation['product_picture'] = None
        return representation


