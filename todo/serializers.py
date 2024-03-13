from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('title', 'created', 'completed')

class TodoSaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('title', 'detail')

class TodoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('title', 'detail', 'created', 'completed')

class TodoModifySerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('title', 'detail', 'completed')