from django.contrib import admin

from social.models import Comment, Post

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
