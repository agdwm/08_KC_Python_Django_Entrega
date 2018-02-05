from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class UserSerializer(serializers.Serializer):

    id = serializers.ReadOnlyField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get('username')
        email = data.get('email')

        if User.objects.filter(username=username).exists():
            raise ValidationError("This user is already in use")

        if User.objects.filter(email=email).exists():
            raise ValidationError("This email is already in use")

        return data


    def create(self, validated_data):
        instance = User()
        instance.first_name = validated_data.get("first_name")
        instance.last_name = validated_data.get("last_name")
        instance.username = validated_data.get("username")
        instance.email =validated_data.get("email")
        instance.set_password(validated_data.get("password"))
        instance.save()
        return instance

    def update(self, instance, validated_data):
        pass

