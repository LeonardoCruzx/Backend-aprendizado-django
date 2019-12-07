from rest_framework import serializers

from .models import *

class PessoaSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nome = serializers.CharField(
        required=True,
        allow_blank=False,
        max_length=30
    )
    idade = serializers.IntegerField(
        required=True,
    )

    def create(self, validated_data):
        return PessoaModel.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.nome = validated_data.get('nome',instance.nome)
        instance.idade = validated_data.get('idade',instance.idade)
        instance.save()
        return instance

