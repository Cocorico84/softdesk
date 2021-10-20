from django.contrib import admin
from .models import Project, Contributor, Comment, Issue

admin.site.register(Project)
admin.site.register(Comment)
admin.site.register(Contributor)
admin.site.register(Issue)
