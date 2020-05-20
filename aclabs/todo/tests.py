import json

from django.utils.timezone import now
from graphene_django.utils.testing import GraphQLTestCase
from todo.schema import schema
from todo.models import Todo




# Create your tests here.
class ListTodosTestCase(GraphQLTestCase):
    # Here you need to inject your test case's schema
    GRAPHQL_SCHEMA = schema
    todo_date = now()

    def setUp(self):
        Todo.objects.create(
            text="TEST",
            priority="MEDIUM",
            completed=True,
            due_date=self.todo_date
            )

    def test_list_query(self):
        query_data = '''
            query list {
                allTodos {
                    text
                    dueDate
                    priority
                    completed
                }
            }
            '''
        response = self.query(query_data, op_name='allTodos')
        self.assertResponseNoErrors(response)
        data = json.loads(response.content.decode())
        todos = data.get("data").get("allTodos")
        assert len(todos) == 1
        actual_todo = todos[0]
        assert actual_todo["text"] == "TEST"
        assert actual_todo["priority"] == "MEDIUM"
        expected = self.todo_date.strftime("%Y-%m-%d")
        assert actual_todo["dueDate"] == expected
        assert actual_todo["completed"] is True

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
