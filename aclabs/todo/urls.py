from django.urls import path

from todo import views

urlpatterns = [
    path('todos', views.todo_list, name="todo-list")
]