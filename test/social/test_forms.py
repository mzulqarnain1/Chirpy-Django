from django.test import TestCase

from social.forms import PostForm, CommentForm


class TestForms(TestCase):

    def test_post_form_valid(self):
        payload = {"body": "New Post"}
        form = PostForm(payload)

        self.assertTrue(form.is_valid())

    def test_post_form_invalid(self):
        payload = {"body": ""}
        form = PostForm(payload)

        self.assertFalse(form.is_valid())
        self.assertEqual(form["body"].errors, ['This field is required.'])

    def test_comment_form_valid(self):
        payload = {"body": "New Post"}
        form = CommentForm(payload)

        self.assertTrue(form.is_valid())

    def test_comment_form_invalid(self):
        payload = {"body": ""}
        form = CommentForm(payload)

        self.assertFalse(form.is_valid())
        self.assertEqual(form["body"].errors, ['This field is required.'])
