from django.contrib import admin
from posts.models import Post,Comment


admin.site.register(Post)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["post", "name", "created"]
    