from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
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


"""class CreateBlogView(LoginRequiredMixin, View):

    def get(self, request):
        pass

    def post(self, request):
        pass"""


class CreatePostView(LoginRequiredMixin, View):

    def get(self, request):
        form = PostForm()
        return render(request, "post_form.html", {'form': form})


    def post(self, request):
        post = Post()
        current_user = post.user
        post.user = request.user #Asignamos al post el usuario autenticado
        post.blog = Blog.objects.get(user=current_user) # Asignamos el post al blog del usuario autenticado
        form = PostForm(request.POST, instance=post)

        if form.is_valid():
            post = form.save()
            form = PostForm()
            url = reverse("post_detail_page", args=[post.user, post.pk])
            message = "¡Post creado con éxito!"
            message += '<a href={0}>View</a>'.format(url)
            messages.success(request, message)
        return render(request, "post_form.html", {'form': form})