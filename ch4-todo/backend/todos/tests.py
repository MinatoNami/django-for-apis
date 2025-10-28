from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Todo


class TodoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        cls.todo = Todo.objects.create(
            title="Test Todo", body="This is a test todo item."
        )

    def test_model_content(self):
        self.assertEqual(self.todo.title, "Test Todo")
        self.assertEqual(self.todo.body, "This is a test todo item.")
        self.assertEqual(str(self.todo), "Test Todo")


class TodoAPITest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.todo = Todo.objects.create(
            title="Test Todo 1", body="This is the first test todo item."
        )
        cls.list_url = reverse("list_todos")
        cls.detail_url = reverse("detail_todo", args=[cls.todo.id])

    def test_list_todos(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Test Todo 1")

    def test_detail_todo(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.todo.title)
        self.assertEqual(response.data["body"], self.todo.body)

    def test_detail_todo_not_found(self):
        response = self.client.get(reverse("detail_todo", args=[999]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
