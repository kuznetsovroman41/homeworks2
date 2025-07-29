from django.shortcuts import get_object_or_404, render,redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from .models import Project, Issue
from .forms import IssueForm, ProjectUserForm
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin

class ProjectListView(ListView):
    model = Project
    paginate_by = 5
    template_name = 'project_list.html'
    context_object_name = 'projects'

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(
                Q(name__icontains=q) | Q(description__icontains=q)
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q', '')
        return context


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'project_detail.html'
    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['issues'] = self.object.issue_set.all()
        context['users'] = self.object.users.all()
        return context


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    fields = ['name', 'description', 'start_date', 'end_date']
    template_name = 'project_form.html'
    success_url = reverse_lazy('webapp:project_list')

class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    fields = ['name', 'description', 'start_date', 'end_date']
    template_name = 'project_form.html'


class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Project
    template_name = 'project_confirm_delete.html'
    success_url = reverse_lazy('webapp:project_list')

class IssueCreateView(LoginRequiredMixin, CreateView):
    model = Issue
    form_class = IssueForm
    template_name = 'issue_form.html'

    def dispatch(self, request, *args, **kwargs):
        self.project_pk = kwargs.get('project_pk')
        self.project = get_object_or_404(Project, pk=self.project_pk)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.project = self.project
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project_pk'] = self.project_pk
        context['project'] = self.project
        return context

    def get_success_url(self):
        return reverse('webapp:project_detail', kwargs={'pk': self.project_pk})



class IssueDetailView(LoginRequiredMixin, DetailView):
    model = Issue
    template_name = 'issue_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project'] = self.object.project
        return context


class IssueUpdateView(LoginRequiredMixin, UpdateView):
    model = Issue
    form_class = IssueForm
    template_name = 'issue_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project_pk'] = self.object.project.pk
        return context

    def get_success_url(self):
        return reverse('webapp:project_detail', kwargs={'pk': self.object.project.pk})



class IssueDeleteView(LoginRequiredMixin, DeleteView):
    model = Issue
    template_name = 'issue_confirm_delete.html'

    def get_success_url(self):
        return reverse('webapp:project_detail', kwargs={'pk': self.object.project.pk})


def manage_project_users(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == 'POST':
        form = ProjectUserForm(request.POST)
        if form.is_valid():
            project.users.set(form.cleaned_data['users'])
            return redirect('webapp:project_detail', pk=project.id)
    else:
        form = ProjectUserForm(initial={'users': project.users.all()})

    return render(request, 'manage_users.html', {'form': form, 'project': project})