from rest_framework import serializers
from rest_framework.fields import Field
from rest_framework.reverse import reverse, reverse_lazy

from blogs.models import Blog, Post


class BlogSerializer(serializers.ModelSerializer):

    blog_url = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = ('id', 'created_at', 'modified_at', 'blog_title', 'description', 'user', 'blog_url')
        read_only_fields = ('created_at', 'modified_at', 'user', 'blog_url')

    def get_blog_url(self, blog):
        return reverse('api_blogs_author', kwargs = {'author': blog.user.username})


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = "__all__"
        read_only_fields = ('created_at', 'modified_at', 'blog')