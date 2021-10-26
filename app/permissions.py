from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsContributor(BasePermission):

    def has_object_permission(self, request, view, obj):
        return (request.user in obj.users.all())


class IsAuthorOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        return (obj.author_user == request.user and request.user  == getattr(obj, "assignee_user", None) or request.method in SAFE_METHODS)
