from social.models import Comment


def get_unseen_notification_count(request):
    if request and request.user and request.user.is_authenticated:
        return {
            "notifications_count": Comment.objects.filter(
                post__author=request.user, seen=False
            )
            .exclude(author=request.user)
            .count()
        }

    return {}
