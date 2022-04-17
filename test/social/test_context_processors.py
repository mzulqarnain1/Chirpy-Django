from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse

from social.models import Comment, Post


class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user("test", "secret")
        self.user2 = User.objects.create_user("test2", "secret")
        self.post = Post.objects.create(body="This is a test post.", author=self.user)
        self.comment = Comment.objects.create(
            body="This is a test comment on user 1's post.",
            author=self.user2,
            post=self.post,
        )

    def test_no_notification_count_without_login(self):
        response = self.client.get(reverse("landing-index"))

        self.assertEqual(response.status_code, 200)
        self.assertNotIn("notifications_count", response.context)

    def test_notification_count_with_login(self):
        self.client.force_login(user=self.user)
        response = self.client.get(reverse("landing-index"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["notifications_count"], 1)
