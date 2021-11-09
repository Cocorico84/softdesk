from authentication.serializers import UserSerializer
from rest_framework.serializers import ModelSerializer

from .models import Comment, Issue, Project


class ProjectSerializer(ModelSerializer):
    users = UserSerializer(read_only=True, many=True)

    class Meta:
        model = Project
        fields = ('title', 'description', 'type', 'users',)

    def validate(self, attrs):
        attrs['author_user_id'] = self.context['request'].user.id
        attrs['users'] = [self.context['request'].user.id]
        return super().validate(attrs)


class IssueSerializer(ModelSerializer):
    class Meta:
        model = Issue
        fields = ('title', 'description', 'tag', 'priority', 'status', 'assignee_user',)

    def validate(self, attrs):
        attrs['project_id'] = self.context.get('request').parser_context.get('kwargs')['project_pk']
        attrs['author_user'] = self.context['request'].user
        return super().validate(attrs)


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ('description',)

    def validate(self, attrs):
        attrs['issue_id'] = self.context.get('request').parser_context.get('kwargs')['issue_pk']
        attrs['author_user_id'] = self.context['request'].user.id
        return super().validate(attrs)
