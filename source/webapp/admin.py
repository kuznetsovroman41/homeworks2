from django.contrib import admin
from .models import Issue, IssueStatus, IssueType

admin.site.register(Issue)
admin.site.register(IssueStatus)
admin.site.register(IssueType)



