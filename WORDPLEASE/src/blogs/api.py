from django.contrib.auth.models import User
from django.utils import timezone
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView, get_object_or_404, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from blogs.models import Blog, Post
from blogs.permissions import PostsPermission
from blogs.serializers import BlogSerializer, PostSerializer, PostListSerializer


class BlogListAPI(ListAPIView):

    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["user__username"]
    ordering_fields = ["blog_title"]


class PostListAPI(ListCreateAPIView):

    queryset = Post.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["post_title", "intro"]
    ordering_fields = ["post_title", "release_date"]

    def get_serializer_class(self):
        return PostListSerializer if self.request.method == "GET" else PostSerializer

    def get_queryset(self):
        author = self.kwargs.get('author')
        get_object_or_404(User, username=author)
        query = Post.objects.filter(blog__user__username=author).order_by("-release_date")
        current_user = self.request.user

        if current_user.is_authenticated and current_user.username==author or current_user.is_superuser:
            return query
        else:
            return query.filter(release_date__lte=timezone.now())

    def perform_create(self, serializer):
        current_blog = Blog.objects.get(user=self.request.user)
        serializer.save(blog=current_blog)


class PostDetailAPI(RetrieveUpdateDestroyAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [PostsPermission]

    def perform_update(self, serializer):
        current_blog = Blog.objects.get(user=self.request.user)
        serializer.save(blog=current_blog)