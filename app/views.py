from rest_framework.viewsets import ModelViewSet, ViewSet
from .models import Project, Issue, Comment
from .serializers import ProjectSerializer, CommentSerializer, IssueSerializer


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = []


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = []

    def get_queryset(self):
        return Comment.objects.filter(issue=self.kwargs['issue_pk'])


class IssueViewSet(ModelViewSet):
    serializer_class = IssueSerializer
    permission_classes = []

    def get_queryset(self):
        return Issue.objects.filter(project=self.kwargs['project_pk'])

