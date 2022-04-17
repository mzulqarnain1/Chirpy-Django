from django.test import TestCase
from django.contrib.auth.models import User

from social.models import Post, Comment


class ModelsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="test", password="test123")
        self.post = Post.objects.create(body="This is a test post.", author=self.user)
        self.comment = Comment.objects.create(
            body="This is a test comment.", author=self.user, post=self.post
        )

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        post = Post.objects.get(author=self.user)
        comment = Comment.objects.get(post=self.post)

        self.assertEqual(str(post), "Post by test")
        self.assertEqual(post.body, "This is a test post.")
        self.assertEqual(comment.body, "This is a test comment.")
