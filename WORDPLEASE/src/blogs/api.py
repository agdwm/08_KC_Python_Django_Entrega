from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from blogs.models import Blog
from blogs.serializers import BlogSerializer


class BlogListAPI(ListAPIView):

    def get(self, request):
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)
