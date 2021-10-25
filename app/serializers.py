from rest_framework.serializers import ModelSerializer
from .models import Project, Issue, Comment
from authentication.serializers import UserSerializer


class ProjectSerializer(ModelSerializer):
    users = UserSerializer(read_only=True, many=True)

    class Meta:
        model = Project
        fields = ('title', 'users')

    def validate(self, attrs):
        attrs['author_user_id'] = self.context['request'].user
        return super().validate(attrs)


class IssueSerializer(ModelSerializer):
    class Meta:
        model = Issue
        fields = ('title', 'tag')

    def validate(self, attrs):
        attrs['author_user_id'] = self.context['request'].user
        return super().validate(attrs)


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', )

    def validate(self, attrs):
        attrs['author_user_id'] = self.context['request'].user
        return super().validate(attrs)
