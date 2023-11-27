from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Task

# Create your views here.


class TaskList(ListView):
    model = Task
    template_name = "main/task_list.html"
    context_object_name = "tasks"


class TaskDetail(DetailView):
    model = Task
    template_name = "main/task_detail.html"
    context_object_name = "task"
