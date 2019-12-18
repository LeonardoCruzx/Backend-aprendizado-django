from rest_framework import serializers

from .models import *



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        user = User.objects.create(
            email = validated_data["email"],
            password = validated_data['password'],
        )
        user.save()
        return user
