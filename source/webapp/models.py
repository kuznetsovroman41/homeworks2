from django.db import models


class IssueStatus(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class IssueType(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Issue(models.Model):
    summary = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    status = models.ForeignKey(IssueStatus, on_delete=models.PROTECT)
    types = models.ManyToManyField(IssueType, related_name='issues')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.summary
