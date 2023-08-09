from rest_framework import serializers
from .models import *

class TaskSerializer(serializers.ModelSerializer):
    """Общий сериалайзер для всех методов"""
    class Meta:
        model = Task
        fields = '__all__'
