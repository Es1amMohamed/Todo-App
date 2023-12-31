from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Task
from django.urls import reverse_lazy

# Create your views here.


class TaskList(ListView):
    model = Task
    template_name = "main/task_list.html"
    context_object_name = "tasks"


class TaskDetail(DetailView):
    model = Task
    template_name = "main/task_detail.html"
    context_object_name = "task"

class TaskCreate(CreateView):
    model = Task
    template_name = "main/task_create.html"
    fields = '__all__'
    success_url = reverse_lazy("task_list")