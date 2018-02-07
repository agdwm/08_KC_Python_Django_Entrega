"""wordplease URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from blogs.api import BlogListAPI, PostListByAuthorAPI, PostDetailAPI
from blogs.views import LatestPostsView, BlogListView, PostListByAuthorView, PostDetailView, CreatePostView
from users.api import UserListAPI, UserDetailAPI
from users.views import LoginView, LogoutView, SignUpView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('login/', LoginView.as_view(), name="login_page"),
    path('logout/', LogoutView.as_view(), name="logout_page"),
    path('singup/', SignUpView.as_view(), name="signup_page"),

    path('new-post/', CreatePostView.as_view(), name="create_post_page"),

    path('blogs/<str:author>/<int:pk>', PostDetailView.as_view(), name="post_detail_page"),
    path('blogs/<str:author>/', PostListByAuthorView.as_view(), name="list_posts_page"),
    path('blogs/', BlogListView.as_view(), name="list_blogs_page"),
    path('', LatestPostsView.as_view(), name="home_page"),

    # API REST
    path('api/1.0/users/<int:pk>', UserDetailAPI.as_view(), name="api_user_detail"),
    path('api/1.0/users/', UserListAPI.as_view(), name="api_users_list"),

    path('api/1.0/blogs/<str:author>/<int:pk>', PostDetailAPI.as_view(), name="api_post_detail"),
    path('api/1.0/blogs/<str:author>/', PostListByAuthorAPI.as_view(), name="api_blogs_author"),
    path('api/1.0/blogs/', BlogListAPI.as_view(), name="api_blogs_list")
]

