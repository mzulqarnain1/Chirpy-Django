from django.test import TestCase

from social.models import Post


class PostTestCase(TestCase):
    def setUp(self):
        Post.objects.create(body="first_post", author=None)
        Post.objects.create(body="second_post", author=None)

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        lion = Post.objects.get(name="lion")
        cat = Post.objects.get(name="cat")
        self.assertEqual(lion.author, None)
        self.assertEqual(cat.speak(), 'The cat says "meow"')
