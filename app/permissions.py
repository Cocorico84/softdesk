from rest_framework.permissions import BasePermission

class IsContributor(BasePermission):

    def has_object_permission(self, request, view, obj):
        return bool(request.user and request.user in obj.get('users'))