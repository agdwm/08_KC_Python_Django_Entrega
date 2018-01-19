from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from blogs.models import Post, Blog


class LatestPostsView(ListView):

    model = Post
    template_name = "home.html"

    def get_queryset(self):
        return Post.objects.all().order_by("-release_date")


class BlogListView(ListView):

    model = Blog
    template_name = "blogs_list.html"
    context_object_name = "blogs"


class PostListByAuthorView(ListView):

    model = Post
    template_name = "blog_author.html"
    context_object_name = "posts"

    def get_queryset(self):
        current_autor = self.kwargs.get('autor')
        return Post.objects.filter(blog__user__username=current_autor).order_by("-release_date")


class PostDetailView(DetailView):

    model = Post
    template_name = "post_detail.html"

    def get_object(self):
        current_autor = self.kwargs.get('autor')
        current_pk = self.kwargs.get("pk")
        possible_posts = Post.objects.filter(blog__user__username=current_autor, pk=current_pk).prefetch_related("category")
        return get_object_or_404(possible_posts)