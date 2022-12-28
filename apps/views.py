from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView

from apps.models import Task


class CustomLoginView(LoginView):
    template_name = 'apps/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')


class MainView(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    login_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(title__icontains=search_input)
        context['search_input'] = search_input
        return context


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'apps/task.html'


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'complete', 'category']
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreateView, self).form_valid(form)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'complete', 'category']
    success_url = reverse_lazy('tasks')


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('tasks')
    context_object_name = 'task'


class RegisterPageView(FormView):
    template_name = 'apps/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPageView, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(RegisterPageView, self).get(*args, **kwargs)
