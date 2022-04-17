from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse

from social.models import Post, Comment


class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user("test", "secret")
        self.user2 = User.objects.create_user("test2", "secret")
        self.post = Post.objects.create(body="This is a test post.", author=self.user)
        self.comment = Comment.objects.create(
            body="This is a test comment.", author=self.user, post=self.post
        )
        self.comment2 = Comment.objects.create(
            body="This is a test comment on user 1's post.",
            author=self.user2,
            post=self.post,
        )

    def test_get_index_page(self):
        resource = response = self.client.get(reverse("landing-index"))

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Login", response.content)

    def test_get_feed_without_login(self):
        response = self.client.get(reverse("feed-index"))

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/landing/?redirect_to=/social/feed/")

    def test_get_feed_with_login(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("feed-index"))

        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context["posts_list"], [self.post])

    def test_make_new_post_invalid_form(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse("feed-index"), data={"body": ""})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["posts_list"]), 1)

    def test_make_new_post(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse("feed-index"), data={"body": "New Post"})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["posts_list"]), 2)

    def test_get_all_comments(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("comments"))

        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context["comments"], [self.comment2])

    def test_get_post_details_page(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("post-details", args=(self.post.id,)))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["post"], self.post)
        self.assertQuerysetEqual(
            response.context["comments"], [self.comment2, self.comment]
        )

    def test_mark_comment_as_seen(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("read-comments", args=(self.comment.id,)))
        comment = Comment.objects.get(pk=self.comment.id)

        self.assertEqual(response.status_code, 302)
        self.assertTrue(comment.seen)

    def test_unauthorized_mark_comment_as_seen(self):
        self.client.force_login(self.user2)
        response = self.client.get(reverse("read-comments", args=(self.comment.id,)))
        comment = Comment.objects.get(pk=self.comment.id)

        self.assertEqual(response.status_code, 401)
        self.assertIn("Unauthorized", str(response.content))

    def test_make_new_comment_invalid(self):
        self.client.force_login(self.user)
        response = self.client.post(
            reverse("post-details", args=(self.post.id,)), data={"body": ""}
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["comments"]), 2)

    def test_make_new_comment(self):
        self.client.force_login(self.user)
        response = self.client.post(
            reverse("post-details", args=(self.post.id,)), data={"body": "New Post"}
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["comments"]), 3)
