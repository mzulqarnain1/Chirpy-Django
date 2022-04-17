from django.forms import CharField, ModelForm, Textarea

from social.models import Post, Comment


class PostForm(ModelForm):
    body = CharField(
        label='',
        widget=Textarea(attrs={
            'rows': 4,
            'placeholder': "Say what's on your mind..."
        })
    )

    class Meta:
        model = Post
        fields = ['body']


class CommentForm(ModelForm):
    body = CharField(
        label='',
        widget=Textarea(attrs={
            'rows': 4,
            'placeholder': "Add a reply..."
        })
    )

    class Meta:
        model = Comment
        fields = ['body']
