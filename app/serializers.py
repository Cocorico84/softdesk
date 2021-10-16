from rest_framework.serializers import ModelSerializer
from .models import Project, Contributor, Issue, Comment


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ('project_id', 'title',)


class ContributorSerializer(ModelSerializer):
    class Meta:
        model = Contributor
        fields = ('user_id',)


class IssueSerializer(ModelSerializer):
    class Meta:
        model = Issue
        fields = ('title',)


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ('comment_id', )
