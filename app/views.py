from rest_framework.viewsets import ModelViewSet
from .models import Project, Issue, Comment
from .serializers import ProjectSerializer, CommentSerializer, IssueSerializer
from .permissions import IsContributor
from rest_framework.permissions import IsAuthenticated

class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated, IsContributor]


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Comment.objects.filter(issue=self.kwargs['issue_pk'])


class IssueViewSet(ModelViewSet):
    serializer_class = IssueSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Issue.objects.filter(project=self.kwargs['project_pk'])

