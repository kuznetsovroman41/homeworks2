from django.contrib import admin
from .models import Issue, IssueStatus, IssueType, Project

admin.site.register(Issue)
admin.site.register(IssueStatus)
admin.site.register(IssueType)
admin.site.register(Project)


