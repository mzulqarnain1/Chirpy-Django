from django.urls import path
from social.views import (
    CommentsListView,
    IndexView,
    PostFeedView,
    PostDetailsView,
    MarkReadView,
)

urlpatterns = [
    path("landing/", IndexView.as_view(), name="landing-index"),
    path("", PostFeedView.as_view(), name="feed-index"),
    path("feed/", PostFeedView.as_view(), name="feed-index"),
    path("post/<int:pk>", PostDetailsView.as_view(), name="post-details"),
    path("comments/", CommentsListView.as_view(), name="comments"),
    path("mark-read/<int:pk>", MarkReadView.as_view(), name="read-comments"),
]
