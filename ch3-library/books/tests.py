from django.test import TestCase
from django.urls import reverse

from .models import Book


class BookTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title="The Great Gatsby",
            subtitle="A Novel",
            author="F. Scott Fitzgerald",
            isbn="9780743273565",
        )

    def test_book_content(self):
        self.assertEqual(self.book.title, "The Great Gatsby")
        self.assertEqual(self.book.subtitle, "A Novel")
        self.assertEqual(self.book.author, "F. Scott Fitzgerald")
        self.assertEqual(self.book.isbn, "9780743273565")

    def test_book_list_view(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "The Great Gatsby")
        self.assertTemplateUsed(response, "books/book_list.html")
