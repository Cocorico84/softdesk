from rest_framework.generics import get_object_or_404
from rest_framework.permissions import SAFE_METHODS, BasePermission

from app.models import Project


class IsAuthorOfProjectOrReadOnly(BasePermission):

    def has_permission(self, request, view) -> bool:
        if view.kwargs.get('project_pk') is not None:
            project = get_object_or_404(Project, id=view.kwargs.get('project_pk'))
            return request.user in project.users.all()
        return True

    def has_object_permission(self, request, view, obj) -> bool:
        if request.method in SAFE_METHODS:
            return request.user in obj.users.all()
        return request.user == obj.author_user


class IsAuthorOfIssueOrReadOnly(BasePermission):

    def has_permission(self, request, view) -> bool:
        if view.kwargs.get('project_pk') is not None:
            project = get_object_or_404(Project, id=view.kwargs.get('project_pk'))
            return request.user in project.users.all()
        return True

    def has_object_permission(self, request, view, obj) -> bool:
        project_users = obj.project.users.all()
        if request.method in SAFE_METHODS:
            return request.user in project_users
        return obj.author_user == request.user


class IsAuthorOfCommentOrReadOnly(BasePermission):

    def has_permission(self, request, view) -> bool:
        if view.kwargs.get('project_pk') is not None:
            project = get_object_or_404(Project, id=view.kwargs.get('project_pk'))
            return request.user in project.users.all()
        return True

    def has_object_permission(self, request, view, obj) -> bool:
        issue_users = obj.issue.project.users.all()
        if request.method in SAFE_METHODS:
            return request.user in issue_users
        return obj.author_user == request.user
