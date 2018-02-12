from rest_framework.permissions import BasePermission


class UsersPermission(BasePermission):

    def has_permission(self, request, view):
        # We are importing "UserDetailAPI" here to avoid the Circular Dependency
        from users.api import UserDetailAPI

        if request.method == "POST" or request.user.is_superuser:
            return True

        if request.method == "GET" and request.user.is_authenticated and isinstance(view, UserDetailAPI):
            return True

        return request.user.is_authenticated and (request.method == "PUT" or request.method == "DELETE")


    def has_object_permission(self, request, view, obj):

        return request.user == obj or request.user.is_superuser

