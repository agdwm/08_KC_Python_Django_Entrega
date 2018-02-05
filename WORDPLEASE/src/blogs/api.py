from rest_framework.response import Response
from rest_framework.views import APIView

from blogs.models import Blog


class BlogListAPI(APIView):

    def get(self, request):
        blogs = Blog.objects.all()
        return Response(blogs)