from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse, reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


from .models import Task


class CustomLoginView(LoginView):
    template_name = 'todo/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('todo:index')


class RegisterPage(FormView):
    template_name = 'todo/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('todo:index')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('todo:index')
        return super(RegisterPage, self).get(*args, **kwargs)


class TaskList(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'todo/index.html'

    def get_context_data(self, **kwargs):
        task_list = Task.objects.filter(user=self.request.user)
        incomplete_tasks = task_list.filter(complete=False)

        search_input = self.request.GET.get('search_area') or ''
        if search_input:
            task_list = task_list.filter(task_name__startswith=search_input)

        context = {"task_list": task_list,
                   "incomplete_tasks": incomplete_tasks,
                   "search_input": search_input, }
        return context

class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'todo/detail.html'


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['task_name', 'description', 'complete']
    success_url = reverse_lazy('todo:index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['task_name', 'description', 'complete']
    success_url = reverse_lazy('todo:index')


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('todo:index')
