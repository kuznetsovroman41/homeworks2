from django import forms
from .models import Issue, IssueStatus, IssueType


class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['summary', 'description', 'status', 'type']

    status = forms.ModelChoiceField(queryset=IssueStatus.objects.all())
    type = forms.ModelChoiceField(queryset=IssueType.objects.all())


