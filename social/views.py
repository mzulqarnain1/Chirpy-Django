from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import HttpResponse, redirect, render
from django.views import View

from social.forms import CommentForm, PostForm
from social.models import Comment, Post


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "social/index.html")


class PostFeedView(LoginRequiredMixin, View):
    login_url = "/landing/"
    redirect_field_name = "redirect_to"

    def get(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by("-created_on")
        form = PostForm()
        context = {"posts_list": posts, "form": form}

        return render(request, "social/feed.html", context)

    def post(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by("-created_on")
        form = PostForm(request.POST)

        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            form = PostForm()

        context = {"posts_list": posts, "form": form}

        return render(request, "social/feed.html", context)


class CommentsListView(LoginRequiredMixin, View):
    login_url = "/landing/"
    redirect_field_name = "redirect_to"

    def get(self, request, *args, **kwargs):
        comments = (
            Comment.objects.filter(
                post__author=request.user,
            )
            .exclude(author=request.user)
            .order_by("seen", "-created_on")
        )

        context = {"comments": comments}
        return render(request, "social/comments.html", context)


class MarkReadView(LoginRequiredMixin, View):
    login_url = "/landing/"
    redirect_field_name = "redirect_to"

    def get(self, request, pk, *args, **kwargs):
        comment = Comment.objects.get(pk=pk)
        if comment.post.author == request.user:
            comment.seen = True
            comment.save()
        else:
            return HttpResponse("Unauthorized", status=401)

        return redirect("/comments/")


class PostDetailsView(LoginRequiredMixin, View):
    login_url = "/landing/"

    def get(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        form = CommentForm()
        comments = Comment.objects.filter(post=post).order_by("-created_on")

        context = {"post": post, "comments": comments, "form": form}
        return render(request, "social/post.html", context)

    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        form = CommentForm(request.POST)
        comments = Comment.objects.filter(post=post).order_by("-created_on")

        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.author = request.user
            new_comment.post = post
            new_comment.save()
            form = CommentForm()

        context = {"post": post, "comments": comments, "form": form}
        return render(request, "social/post.html", context)
