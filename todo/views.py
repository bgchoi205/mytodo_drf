from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.generics import get_object_or_404

from .models import Todo
from .serializers import TodoSerializer, TodoSaveSerializer, TodoDetailSerializer, TodoModifySerializer, TodoDoneSerializer

# Create your views here.
class TodoListView(APIView):
    def get(self, request):
        todos = Todo.objects.filter(completed = False)
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class TodoSaveView(APIView):
    def post(self, request):
        serializer = TodoSaveSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class TodoDetailView(APIView):
    def get(self, request, pk):
        todo = get_object_or_404(Todo, id=pk)
        serializer = TodoDetailSerializer(todo)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        todo = get_object_or_404(Todo, id=pk)
        serializer = TodoModifySerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DoneTodoListView(APIView):
    def get(self, request):
        todos = Todo.objects.filter(completed=True)
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class DoneTodoView(APIView):
    def put(self, request, pk):
        todo = get_object_or_404(Todo, id=pk)
        todo.completed = True
        todo.save()
        serializer = TodoDoneSerializer(todo)
        
        return Response(status=status.HTTP_200_OK)
        