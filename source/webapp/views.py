from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import Issue
from .forms import IssueForm


class IssueListView(TemplateView):
    template_name = 'issue_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['issues'] = Issue.objects.all().order_by('-created_at')
        return context


class IssueDetailView(DetailView):
    model = Issue
    template_name = 'issue_detail.html'


class IssueCreateView(CreateView):
    model = Issue
    form_class = IssueForm
    template_name = 'issue_form.html'
    success_url = reverse_lazy('issue_list')


class IssueUpdateView(UpdateView):
    model = Issue
    form_class = IssueForm
    template_name = 'issue_form.html'
    success_url = reverse_lazy('issue_list')


class IssueDeleteView(DeleteView):
    model = Issue
    template_name = 'issue_confirm_delete.html'
    success_url = reverse_lazy('issue_list')

