from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from aplicatie1.models import Todo


class TodoView(LoginRequiredMixin, ListView):
    model = Todo
    template_name = 'aplicatie1/todo_index.html'
    paginate_by = 5
    queryset = model.objects.filter(status="Pending")
    context_object_name = 'todo'


    def get_context_data(self, *args, **kwargs):
        data = super(TodoView, self).get_context_data(*args, **kwargs)
        return data


class CreateTodoView(LoginRequiredMixin, CreateView):
    model = Todo
    fields = ['task', 'responsible', 'description', 'task_creation_date', 'wished_due_date', 'estimated_duration']
    template_name = 'aplicatie1/todo_form.html'

    def get_success_url(self):
        return reverse('todo:lista_todo')


class UpdateTodoView(LoginRequiredMixin, UpdateView):
    model = Todo
    fields = ['task', 'responsible', 'description', 'task_creation_date', 'wished_due_date', 'estimated_duration', 'status']
    template_name = 'aplicatie1/todo_form.html'

    def get_success_url(self):
        return reverse('todo:lista_todo')

@login_required
def delete_todo(request, pk):
    Todo.objects.filter(id=pk).update(active=0, status="Deleted")
    return redirect('todo:lista_todo')

@login_required
def activate_task(request, pk):
    Todo.objects.filter(id=pk).update(active=1)
    return redirect('todo:lista_todo')


class DeleteTask(LoginRequiredMixin, UpdateView):
    model = Todo
    template_name = 'aplicatie1/todo_index.html'
    paginate_by = 5
    queryset = model.objects.filter(status="Deleted")
    context_object_name = 'todo'

    def get_context_data(self, *args, **kwargs):
        data = super(DeleteTask, self).get_context_data(*args, **kwargs)
        return data


class DeletedTasksView(LoginRequiredMixin, ListView):
    model = Todo
    template_name = 'aplicatie1/todo_index.html'
    paginate_by = 5
    queryset = model.objects.filter(status="Deleted")
    context_object_name = 'todo'

    def get_context_data(self, *args, **kwargs):
        data = super(DeletedTasksView, self).get_context_data(*args, **kwargs)
        return data


class TaskDoneView(LoginRequiredMixin, ListView):
    model = Todo
    template_name = 'aplicatie1/todo_index.html'
    paginate_by = 5
    queryset = model.objects.filter(status="Done")
    context_object_name = 'todo'

    def get_context_data(self, *args, **kwargs):
        data = super(TaskDoneView, self).get_context_data(*args, **kwargs)
        return data


