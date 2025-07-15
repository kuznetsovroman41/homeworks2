from django.db import models
from .validation import validate_no_bug_in_summary, validate_summary_length


class IssueStatus(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class IssueType(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Issue(models.Model):
    summary = models.CharField(
        max_length=100,
        validators=[validate_summary_length, validate_no_bug_in_summary],
        verbose_name='Краткое описание'
    )
    description = models.TextField(verbose_name='Полное описание', blank=True)
    status = models.ForeignKey('IssueStatus', on_delete=models.CASCADE, verbose_name='Статус')
    types = models.ManyToManyField('IssueType', verbose_name='Тип')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return self.summary
