from rest_framework import serializers
# from django_celery_results.models import TaskResult
from .models import TaskResult

class entrySerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskResult 
        fields = ('task_name', 'task_id', 'task_status')