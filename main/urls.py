from django.urls import path, include
from . import views

app_name = "main"

urlpatterns = [
    path("", views.TaskList.as_view(), name="task_list"),
    path("task/<str:slug>/", views.TaskDetail.as_view(), name="task_detail"),
    path("create/task/", views.TaskCreate.as_view(), name="task_create"),
]
