from rest_framework import serializers

from django.contrib.auth.hashers import make_password

from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        user = User.objects.create(
            nick=validated_data['nick'],
            username=validated_data['username'],
            password=make_password(validated_data['password'])
        )
        user.save()
        return user
