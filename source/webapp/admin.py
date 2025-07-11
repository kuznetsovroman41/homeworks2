from django.contrib import admin
from .models import IssueStatus, IssueType, Issue

admin.site.register(IssueStatus)
admin.site.register(IssueType)
admin.site.register(Issue)


