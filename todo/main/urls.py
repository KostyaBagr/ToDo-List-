from django.urls import path
from .views import *

urlpatterns = [
    path('api/tasks/',GetTasksListView.as_view(), name='tasks'),
    path('api/tasks/create/',CreateTasksListView.as_view(), name='create_task' ),
    path('api/tasks/detail/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
]