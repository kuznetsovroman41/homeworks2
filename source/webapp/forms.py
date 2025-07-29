from django import forms
from .models import Issue, IssueStatus, IssueType
from django.contrib.auth import get_user_model

class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['summary', 'description', 'status', 'types']
        widgets = {
            'types': forms.CheckboxSelectMultiple()
        }

    status = forms.ModelChoiceField(queryset=IssueStatus.objects.all())
    types = forms.ModelMultipleChoiceField(
        queryset=IssueType.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

User = get_user_model()

class ProjectUserForm(forms.Form):
    users = forms.ModelMultipleChoiceField(
        queryset=User.objects.none(),
        widget=forms.CheckboxSelectMultiple
    )

    def __init__(self, *args, **kwargs):
        queryset = kwargs.pop('queryset', None)
        super().__init__(*args, **kwargs)
        if queryset is not None:
            self.fields['users'].queryset = queryset
        else:
            self.fields['users'].queryset = User.objects.all()
