from rest_framework import serializers

from .models import *

from django.core.mail import send_mail

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        user = User.objects.create_user(
            email = validated_data["email"],
            password = validated_data['password'],
        )
        send_mail('cadastro',f'ola seja bem vindo {user.nick} ao nosso site','coding.in.python.nao.responda@gmail.com',[user.email],fail_silently=False)
        return user

    def to_representation(self, instance):
        representation = super(UserSerializer, self).to_representation(instance)
        try:
            representation['profile_picture'] = instance.profile_picture.url
        except:
            representation['profile_picture'] = None
        return representation