from django.contrib import admin
from django.urls import path
from .views import TodoView

urlpatterns = [
    path("", TodoView.as_view()),
]
