# django imports
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

# installed apps imports
from graphene_django.views import GraphQLView

# our app imports
from todo import views

urlpatterns = [
    path('todos', views.todo_list, name="todo-list"),
    path('graphqlapi/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=False))),
]