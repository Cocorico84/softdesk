from django.conf import settings
from django.db import models

TYPES = (
    ("BACKEND", "back-end"),
    ("FRONTEND", "front-end"),
    ("IOS", "iOS"),
    ("ANDROID", "Android"),
)

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
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=128, blank=True)
    type = models.CharField(max_length=32, blank=True, choices=TYPES)
    author_user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='projects')
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='user_projects')

    def __str__(self) -> str:
        return self.title


class Issue(models.Model):
    title = models.CharField(max_length=64, blank=True)
    description = models.CharField(max_length=128, blank=True)
    tag = models.CharField(max_length=32, choices=TAGS, blank=True)
    priority = models.CharField(max_length=32, choices=PRIORITIES, blank=True)
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name='issues')
    status = models.CharField(max_length=32, choices=STATUS, blank=True)
    author_user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='issues')
    assignee_user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='assigned_issues', null=True)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    description = models.CharField(max_length=128)
    author_user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.description
