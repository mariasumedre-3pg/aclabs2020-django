from django.shortcuts import render

from todo.models import Todo

# Create your views here.
def todo_list(request):
    todos = Todo.objects.all()
    context = {'todos': todos}
    return render(request, 'todo/todo-list.html', context)


def index(request):
    endpoint = 'graphql'
    url = "{scheme}://{host}/{endpoint}".format(
        scheme=request.scheme,
        host=request.get_host(),
        endpoint=endpoint
    )
    context = {'grapql_endpoint': endpoint}
    return render(request, 'todo/index.html', context)
