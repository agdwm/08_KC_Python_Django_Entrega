from django.contrib.auth.models import User
from django.views.generic import ListView

from blogs.models import Post, Blog


class LatestPosts(ListView):

    model = Post
    template_name = "home.html"

    def get_queryset(self):
        return Post.objects.all().order_by("-release_date")[:4]


class ListBlogs(ListView):

    model = Blog
    template_name = "blogs.html"
    context_object_name = "blogs"
    queryset = Blog.objects.all()


class ListPosts(ListView):

    model = Post
    template_name = "posts_list.html"
    context_object_name = "posts"

    def get_queryset(self):
        autor = self.kwargs.get('autor')
        return Post.objects.filter(blog__user__username=autor).order_by("-release_date")