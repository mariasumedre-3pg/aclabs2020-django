import json

from graphene_django.utils.testing import GraphQLTestCase
from todo.schema import schema
from todo.models import Todo

# Create your tests here.
class ListTodosTestCase(GraphQLTestCase):
    # Here you need to inject your test case's schema
    GRAPHQL_SCHEMA = schema

    def setUp(self):
        Todo.objects.create(
            text="TEST"
        )

    def test_edit_mutation(self):
        todo_id = Todo.objects.last().id
        data = """
                mutation editTodo {{
                    editTodo(
                        id: "{}"
                        text: "TEST2"
                    ) {{
                        todo {{
                            text
                        }}
                    }}
                }}""".format(str(todo_id))
        response = self.query(data, op_name='editTodo')
        self.assertResponseNoErrors(response)
        data = json.loads(response.content.decode())
        actual = data.get("data").get("editTodo").get("todo").get("text")
        assert actual == "TEST2"

    def tearDown(self):
        Todo.objects.all().delete()
