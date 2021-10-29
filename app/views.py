from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Comment, Issue, Project
from .permissions import IsAuthorOfIssueOrReadOnly, IsAuthorOfProjectOrReadOnly, IsAuthorOfCommentOrReadOnly
from .serializers import CommentSerializer, IssueSerializer, ProjectSerializer
from app.models import Project
from app.permissions import IsAuthorOfProjectOrReadOnly
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from authentication.models import User
from authentication.serializers import UserSerializer
from rest_framework.status import HTTP_201_CREATED
class ProjectViewSet(ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated, IsAuthorOfProjectOrReadOnly]

    def get_queryset(self):
        return Project.objects.filter(users=self.request.user)


class IssueViewSet(ModelViewSet):
    serializer_class = IssueSerializer
    permission_classes = [IsAuthenticated, IsAuthorOfIssueOrReadOnly]

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        data['assignee_user'] = data.get("assignee_user", request.user.id)
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=HTTP_201_CREATED, headers=headers)

    def get_queryset(self):
        return Issue.objects.filter(project=self.kwargs['project_pk'])


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsAuthorOfCommentOrReadOnly]

    def get_queryset(self):
        return Comment.objects.filter(issue=self.kwargs['issue_pk'])


class UserViewSet(ViewSet):
    permission_classes = [IsAuthenticated, IsAuthorOfProjectOrReadOnly]

    def list(self, request, project_pk):
        queryset = User.objects.filter(user_projects__id=project_pk)
        if queryset == queryset.none():
            raise ValidationError("No user in this project")
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, project_pk, user_id, *args, **kwargs):
        user = get_object_or_404(User, id=user_id)
        project = Project.objects.get(pk=project_pk)
        if user in project.users.all():
            raise ValidationError("The user is already in the list.")
        else:
            project.users.add(user.id)

        serializer = UserSerializer(user)
        return Response(serializer.data)

    def destroy(self, request, project_pk, user_id, *args, **kwargs):
        project = Project.objects.get(pk=project_pk)
        user = User.objects.filter(id=user_id).first()
        if user is None:
            raise ValidationError("The user doesn't exist.")
        project.users.remove(user_id)
        serializer = UserSerializer(user)
        return Response(serializer.data)
