from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.generics import ListAPIView, get_object_or_404, ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from blogs.models import Blog, Post
from blogs.serializers import BlogSerializer, PostSerializer


class BlogListAPI(ListAPIView):
    
    def get(self, request):
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)


class PostListByAuthorAPI(ListCreateAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        author = self.kwargs.get('author')
        get_object_or_404(User, username=author)
        return Post.objects.filter(blog__user__username=author).order_by("-release_date")


    def perform_create(self, serializer):
        current_blog = Blog.objects.get(user=self.request.user)
        serializer.save(blog=current_blog)

