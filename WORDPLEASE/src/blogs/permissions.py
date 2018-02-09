from django.utils import timezone
from rest_framework.permissions import BasePermission

from blogs.models import Post


class PostsPermission(BasePermission):

    #authentication
    def has_permission(self, request, view):
        return request.method == "GET" or request.user.is_authenticated

    #permission
    def has_object_permission(self, request, view, obj):
        permission = False

        if request.method == "GET":
            if obj.release_date <= timezone.now():
                permission = True
            else:
                if obj.blog.user == request.user or request.user.is_superuser:
                    permission = True
        elif obj.blog.user == request.user or request.user.is_superuser:
            permission = True
        return permission

