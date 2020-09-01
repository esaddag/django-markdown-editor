from django.test import TestCase
from app.models import Post

class PostTestCase(TestCase):
    def testPost(self):
        post = Post(title="My Title", description="Test description", wiki="Post body")
        self.assertEqual(post.title, "My Title")
        self.assertEqual(post.description, "Test description")
        self.assertEqual(post.wiki, "Post body")