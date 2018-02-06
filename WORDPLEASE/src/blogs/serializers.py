from rest_framework import serializers
from rest_framework.fields import Field
from rest_framework.reverse import reverse, reverse_lazy

from blogs.models import Blog


class BlogSerializer(serializers.ModelSerializer):

    blog_url = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = ('id', 'created_at', 'modified_at', 'blog_title', 'description', 'user', 'blog_url')
        read_only_fields = ('created_at', 'modified_at', 'blog_url')

    def get_blog_url(self, blog):
        return reverse('api_blogs_author', args=[blog.user.username])

