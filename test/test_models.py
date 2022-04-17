from django.test import TestCase
from django.contrib.auth.models import User

from social.models import Post


class PostTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test', password='test123')
        Post.objects.create(body="This is a test post.", author=self.user)

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        posts = Post.objects.get(author=self.user)
        self.assertEqual(posts.body, "This is a test post.")
