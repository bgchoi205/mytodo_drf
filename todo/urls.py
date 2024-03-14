from django.contrib import admin
from django.urls import path
from .views import TodoListView, TodoSaveView, TodoDetailView, DoneTodoListView, DoneTodoView

urlpatterns = [
    path("", TodoListView.as_view()),
    path("save/", TodoSaveView.as_view()),
    path("<int:pk>/", TodoDetailView.as_view()),
    path("done/", DoneTodoListView.as_view()),
    path("done/<int:pk>/", DoneTodoView.as_view())
]
