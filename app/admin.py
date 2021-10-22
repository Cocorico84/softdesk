from django.contrib import admin
from .models import Project, Comment, Issue

admin.site.register(Project)
admin.site.register(Comment)
admin.site.register(Issue)
