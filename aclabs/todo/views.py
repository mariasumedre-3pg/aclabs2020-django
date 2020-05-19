from django.shortcuts import render

from todo.models import Todo

# Create your views here.
def todo_list(request):
    todos = Todo.objects.all()
    context = {'todos': todos}
    return render(request, 'todo/todo-list.html', context)
