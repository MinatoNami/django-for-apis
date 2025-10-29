from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import Post


class BlogTestCase(TestCase):
    @classmethod
    def setUp(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser", email="testuser@example.com", password="testpassword"
        )
        cls.post = Post.objects.create(
            title="Test Post", content="This is a test post.", author=cls.user
        )

    def test_post_creation(self):
        self.assertEqual(self.post.title, "Test Post")
        self.assertEqual(self.post.content, "This is a test post.")
        self.assertEqual(self.post.author.username, "testuser")
