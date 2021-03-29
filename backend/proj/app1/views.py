from django.http import HttpResponse

# from django_celery_results.models import TaskResult
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import entrySerializer

from .models import TaskResult
from .tasks import add, mul

from celery.result import AsyncResult


def getStatus(_taskid):
    return str(AsyncResult(_taskid).state)

def spawnTask(task_id, task_name):
    Obj = TaskResult.objects.create() 
    Obj.task_name = task_name 
    Obj.task_id = task_id 
    Obj.task_status = getStatus(task_id)
    Obj.save()


class trial1(APIView):
    def get(self, request, *args, **kwargs):
        qs = TaskResult.objects.all().order_by('pk').reverse()
        for task in qs : 
            task.task_status = getStatus(task.task_id)
            task.save()
        serialized_data = entrySerializer(qs, many=True)
        return Response(serialized_data.data)

    def post(self, request, *args, **kwargs):
        spawnTask(add.delay(3, 5), "add_task")
        # mul.delay(10, 5)
        return Response()