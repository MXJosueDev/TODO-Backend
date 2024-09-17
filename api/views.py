from django.http import request, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions, viewsets
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema

from .models import Task, List
from .serializers import TaskSerializer, ListSerializer

def checkTask(pk):
    try:
        return Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return False 

def checkList(uuid):
    try:
        return List.objects.get(pk=uuid)
    except List.DoesNotExist:
        return False

# Create your views here.
class ListCreateView(APIView):
    serializer_class = ListSerializer

    @extend_schema(
        request=ListSerializer,
        responses={201: ListSerializer}
    )
    def post(self, request):
        data = JSONParser().parse(request)
        serializer = ListSerializer(List.create(), data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

        return JsonResponse(serializer.errors, status=400)

class ListCrudView(APIView):    
    serializer_class = ListSerializer

    @extend_schema(
        responses={200: ListSerializer, 404: None}
    )
    def get(self, request, uuid):
        list = checkList(uuid)

        if not list:
            return HttpResponse(status=404)

        serializer = ListSerializer(list)

        return JsonResponse(serializer.data, safe=False)

    """ @extend_schema(
        responses={204: None, 404: None}
    )
    def delete(self, request, uuid):
        list = checkList(uuid)

        if not list:
            return HttpResponse(status=404)

        list.delete()

        return HttpResponse(status=204) """

    @extend_schema(
        request=ListSerializer(partial=True),
        responses={
            201: ListSerializer,
            404: None
        }
    )
    def patch(self, request, uuid):
        list = checkList(uuid)

        if not list:
            return HttpResponse(status=404)

        data = JSONParser().parse(request)
        serializer = ListSerializer(list, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        
        return HttpResponse(status=400)

class ListTasksView(APIView):
    serializer_class = TaskSerializer

    @extend_schema(
        responses={200: TaskSerializer(many=True), 404: None}
    )
    def get(self, request, uuid):
        list = checkList(uuid)
        if not list:
            return HttpResponse(status=404)

        tasks = list.get_tasks()
        serializer = TaskSerializer(tasks, many=True)

        return JsonResponse(serializer.data, safe=False)

    @extend_schema(
        request=TaskSerializer,
        responses={201: TaskSerializer}
    )
    def post(self, request, uuid):
        list = checkList(uuid)
        if not list:
            return HttpResponse(status=404)

        data = JSONParser().parse(request)
        task = list.add_task(data['title'])

        serializer = TaskSerializer(task, data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

        return JsonResponse(serializer.errors, status=400)

class ListTasksCrudView(APIView):
    serializer_class = TaskSerializer

    @extend_schema(
        request=TaskSerializer(partial=True),
        responses={
            201: TaskSerializer,
            404: None
        }
    )
    def patch(self, request, uuid, task_pk):
        list = checkList(uuid)
        if not list:
            return HttpResponse(status=404)

        task = checkTask(task_pk)
        if not task:
            return HttpResponse(status=404)

        data = JSONParser().parse(request)
        serializer = TaskSerializer(task, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

        return JsonResponse(serializer.errors, status=400)

    @extend_schema(
        responses={
            204: None,
            404: None
        }
    )
    def delete(self, request, uuid, task_pk):
        list = checkList(uuid)
        if not list:
            return HttpResponse(status=404)

        task = checkTask(task_pk)
        if not task:
            return HttpResponse(status=404)
        
        task.delete()

        return HttpResponse(status=204)

class TasksListView(APIView):
    serializer_class = TaskSerializer

    @extend_schema(
        responses={
            200: TaskSerializer(many=True),
        }
    )
    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)

        return JsonResponse(serializer.data, safe=False)

    @extend_schema(
        request=TaskSerializer
    )
    def post(self, request):
        data = JSONParser().parse(request)
        serializer = TaskSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

        return JsonResponse(serializer.errors, status=400)        

class TaskEditView(APIView):
    serializer_class = TaskSerializer

    @extend_schema(
        request=TaskSerializer(partial=True),
        responses={
            201: TaskSerializer,
            404: None
        }
    )
    def patch(self, request, pk):
        task = checkTask(pk)
        if(not task):
            return HttpResponse(status=404)

        data = JSONParser().parse(request)
        serializer = TaskSerializer(task, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=404)

    @extend_schema(
        responses={
            204: None,
            404: None
        }
    )
    def delete(self, request, pk):
        task = checkTask(pk)
        if(not task):
            return HttpResponse(status=404)
            
        task.delete()

        return HttpResponse(status=204)