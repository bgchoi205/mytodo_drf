from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets

from .models import Todo
from .serializers import TodoSerializer

# Create your views here.
class TodoView(APIView):
    def get(self, request):
        todos = Todo.objects.filter(completed = False)
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)