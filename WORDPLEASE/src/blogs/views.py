from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.views import View
from django.views.generic import ListView, DetailView

from blogs.models import Post, Blog
from users.forms import PostForm


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
        current_author = self.kwargs.get('author')
        get_object_or_404(User, username=current_author)
        return Post.objects.filter(blog__user__username=current_author).order_by("-release_date")

class PostDetailView(DetailView):

    model = Post
    template_name = "post_detail.html"

    def get_object(self):
        current_author = self.kwargs.get('author')
        current_pk = self.kwargs.get("pk")
        possible_posts = Post.objects.filter(blog__user__username=current_author, pk=current_pk).prefetch_related("category")
        return get_object_or_404(possible_posts)


class CreatePostView(LoginRequiredMixin, View):

    def get(self, request):
        form = PostForm()
        return render(request, "post_form.html", {'form': form})


    def post(self, request):
        post = Post()

        # Asignamos el post al blog del usuario autenticado
        post.blog = Blog.objects.get(user=request.user)
        form = PostForm(request.POST, instance=post)

        if form.is_valid():
            post = form.save()
            form = PostForm()
            url = reverse("post_detail_page", args=[request.user, post.pk])
            message = "¡Post creado con éxito!"
            message += mark_safe('<a href={0}> Ver post </a>'.format(url))
            messages.success(request, message)
        #else:
            #form.add_error(None, "El formulario no es válido")

        return render(request, "post_form.html", {'form': form})