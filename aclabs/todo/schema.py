import graphene
from graphene_django.types import DjangoObjectType

from todo.models import Todo


class TodoType(DjangoObjectType):
    class Meta:
        model = Todo


class Query(graphene.ObjectType):
    all_todos = graphene.List(TodoType)
    todo = graphene.Field(
        TodoType,
        id=graphene.String(),
        text=graphene.String()
    )

    def resolve_all_todos(self, info, **kwargs):
        return Todo.objects.all()

    def resolve_todo(self, info, **kwargs):
        _id = kwargs.get("id")
        _text = kwargs.get("text")
        if _id:
            return Todo.objects.get(id=_id)
        if _text:
            return Todo.objects.get(text=_text)
        return None


class AddTodoInput(graphene.InputObjectType):
    text = graphene.String()
    priority = graphene.String()
    dueDate = graphene.String()
    completed = graphene.Boolean()


class AddTodoMutation(graphene.Mutation):
    class Arguments:
        todo = AddTodoInput(required=True)

    todo = graphene.Field(TodoType)

    def mutate(self, info, todo):
        new_todo = Todo.objects.create(
            text=todo.text,
            priority=todo.priority or "LOW"
        )
        return AddTodoMutation(todo=new_todo)


class TodoMutation(graphene.Mutation):
    class Arguments:
        id = graphene.String(required=True)
        text = graphene.String()
        priority = graphene.String()
        dueDate = graphene.String()
        completed = graphene.Boolean()
    todo = graphene.Field(TodoType)

    def mutate(self, info, id, text=None, priority=None, dueDate=None, completed=False):
        todo = Todo.objects.get(pk=id)
        if text is not None:
            todo.text = text
        if priority:
            todo.priority = priority
        if dueDate:
            todo.due_date = datetime.datetime.fromisoformat(dueDate)
        todo.completed = completed
        todo.save()
        return TodoMutation(todo=todo)


class DeleteTodoMutation(graphene.Mutation):
    class Arguments:
        id = graphene.String(required=True)

    ok = graphene.Boolean()

    def mutate(self, info, **kwargs):
        deleted = False
        _id = kwargs.get("id")
        if _id:
            todo = Todo.objects.get(id=_id)
            count, _ = todo.delete()
            if count == 1:
                deleted = True
        return DeleteTodoMutation(ok=deleted)


class Mutation(graphene.ObjectType):
    edit_todo = TodoMutation.Field()
    add_todo = AddTodoMutation.Field()
    delete_todo = DeleteTodoMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)