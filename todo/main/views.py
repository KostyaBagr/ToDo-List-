from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import *
from rest_framework.permissions import AllowAny
from rest_framework import generics
from .serializers import *
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
# Create your views here.

class TaskFilter:
    """Фильтрация задач"""
    def filter_tasks(self, queryset, status):
        if status == 'completed':
            return queryset.filter(is_completed=True)
        elif status == 'not_completed':
            return queryset.filter(is_completed=False)
        return queryset


class GetTasksListView(APIView,TaskFilter):
    """
         <<Получение списка задач>>
         Query parameters:
             - status: Статус задачи (all, completed, not_completed)
        """
    status_param_config = openapi.Parameter('status', in_=openapi.IN_QUERY, description='Отфильтруйте запрос по статусу выполнения',
                                                type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[status_param_config])
    def get(self,request):
        try:
            queryset = Task.objects.all()
            status = self.request.query_params.get('status', 'all')
            filtered_queryset = self.filter_tasks(queryset, status)
            serializer = TaskSerializer(filtered_queryset, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error':"Ошибка запроса"})


class CreateTasksListView(generics.CreateAPIView):
    """Создание задачи"""
    permission_classes = [AllowAny]
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)



class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Получени задачи по id, ее удаление и изменение"""
    permission_classes = [AllowAny]
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

