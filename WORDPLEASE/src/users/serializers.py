from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from blogs.models import Blog


class UserListSerializer(serializers.Serializer):


    id = serializers.ReadOnlyField()
    username = serializers.CharField()
    email = serializers.EmailField()
    blog_title = serializers.SerializerMethodField()

    def get_blog_title(self, obj):
        return obj.blog_set.values_list('blog_title', flat=True)[0]


class UserSerializer(UserListSerializer):

    first_name = serializers.CharField()
    last_name = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get('username')
        email = data.get('email')
        blog_title = self.initial_data.get('blog_title')

        # Create user
        if self.instance is None:
            if User.objects.filter(username=username).exists():
                raise ValidationError("This username already exists")
            if User.objects.filter(email=email).exists():
                raise ValidationError("This email already exists")
            if Blog.objects.filter(blog_title=blog_title).exists():
                raise ValidationError("This blog title already exists")

        # Update user
        if self.instance:
            if self.instance.username != username and User.objects.filter(username=username).exists():
                raise ValidationError("Wanted username is already in use")
            if self.instance.email != email and User.objects.filter(email=email).exists():
                raise ValidationError("Wanted email is already in use")
            if not self.instance.blog_set.filter(blog_title=blog_title).exists():
                if Blog.objects.filter(blog_title=blog_title).exists():
                    raise ValidationError("Wanted blog title is already in use")
        return data


    def create(self, validated_data):
        instance = User()
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


    def update(self, instance, validated_data):

        instance.first_name = validated_data.get("first_name")
        instance.last_name = validated_data.get("last_name")
        instance.username = validated_data.get("username")
        instance.email = validated_data.get("email")
        instance.set_password(validated_data.get("password"))

        instance.save()

        instance.blog_set.update(blog_title=self.initial_data.get('blog_title'), user=instance)

        return instance