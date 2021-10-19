from django.db import models
from django.conf import settings

PERMISSIONS = ()
PRIORITIES = (
    ('LOW', 'low'),
    ('MEDIUM', 'medium'),
    ('HIGH', 'high'),
)
TAGS = (
    ('BUG', 'bug'),
    ('IMPROVE', 'improve'),
    ('TASK', 'task'),
)
STATUS = (
    ('TODO', 'todo'),
    ('DOING', 'doing'),
    ('DONE', 'done'),
    )


class Project(models.Model):
    project_id = models.IntegerField()
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=128, blank=True)
    type = models.CharField(max_length=32, blank=True)
    author_user_id = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='projects')


class Contributor(models.Model):
    user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='contributors')
    project_id = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name='contributors')
    permission = models.CharField(max_length=32, choices=PERMISSIONS)
    role = models.CharField(max_length=64)


class Issue(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=128)
    tag = models.CharField(max_length=32, choices=TAGS)
    priority = models.CharField(max_length=32, choices=PRIORITIES)
    project_id = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name='issues')
    status = models.CharField(max_length=32, choices=STATUS)
    author_user_id = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='issues')
    assignee_user_id = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='assigned_issues')
    created_time = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    comment_id = models.IntegerField()
    description = models.CharField(max_length=128)
    author_user_id = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    issue_id = models.ForeignKey(Issue, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
