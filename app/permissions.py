from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsContributor(BasePermission):

    def has_object_permission(self, request, view, obj):
        return (request.user in obj.users)


class IsAuthorOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        return (obj.author == request.user and request.user in obj.assignee_user or request.method in SAFE_METHODS)
