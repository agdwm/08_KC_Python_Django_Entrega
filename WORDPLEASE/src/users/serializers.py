from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from blogs.models import Blog
from blogs.serializers import BlogSerializer


class UserListSerializer(serializers.Serializer):

    id = serializers.ReadOnlyField()
    username = serializers.CharField()
    email = serializers.EmailField()


class UserSerializer(UserListSerializer):

    first_name = serializers.CharField()
    last_name = serializers.CharField()
    password = serializers.CharField()
    #blog_title = serializers.PrimaryKeyRelatedField(read_only=True)

    def validate(self, data):
        username = data.get('username')
        email = data.get('email')
        blog_title = data.get('blog_title')

        # Create user
        if self.instance is None:
            if User.objects.filter(username=username).exists():
                raise ValidationError("This username already exists")
            if User.objects.filter(email=email).exists():
                raise ValidationError("This email already exists")

        # Update user
        if self.instance:
            if self.instance.username != username and User.objects.filter(username=username).exists():
                raise ValidationError("Wanted username is already in use")
            if self.instance.email != email and User.objects.filter(email=email).exists():
                raise ValidationError("Wanted email is already in use")
        return data


    def create(self, validated_data):
        instance = User()
        return self.update(instance, validated_data)

    def update(self, instance, validated_data):
        blog = Blog()
        instance.first_name = validated_data.get("first_name")
        instance.last_name = validated_data.get("last_name")
        instance.username = validated_data.get("username")
        instance.email = validated_data.get("email")
        instance.set_password(validated_data.get("password"))
        instance.save()

        blog.blog_title = self.initial_data.get('blog_title')
        blog.user = instance
        blog.save()

        return instance