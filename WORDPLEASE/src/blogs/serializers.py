from rest_framework import serializers
from rest_framework.reverse import reverse

from blogs.models import Blog, Post


class BlogSerializer(serializers.ModelSerializer):

    blog_url = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = ('id', 'created_at', 'modified_at', 'blog_title', 'description', 'user', 'blog_url')
        read_only_fields = ('created_at', 'modified_at', 'user', 'blog_url')

    def get_blog_url(self, blog):
        return reverse('api_blogs_author', kwargs = {'author': blog.user.username})



class PostListSerializer(serializers.ModelSerializer):

    author = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('id', 'post_title', 'image', 'video', 'intro', 'release_date', 'author')

    def get_author(self, obj):
        divider = " "
        username = obj.blog.user.username
        last_name = obj.blog.user.last_name
        seq = (username, last_name)
        return divider.join(seq)



class PostSerializer(PostListSerializer):

    blog = BlogSerializer(read_only=True)

    class Meta:
        model = Post
        fields = "__all__"
        extra_fields = ['author']