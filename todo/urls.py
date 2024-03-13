from django.contrib import admin
from django.urls import path
from .views import TodoListView, TodoSaveView, TodoDetailView

urlpatterns = [
    path("", TodoListView.as_view()),
    path("save/", TodoSaveView.as_view()),
    path("<int:pk>/", TodoDetailView.as_view())
]
