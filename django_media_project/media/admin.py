from django.contrib import admin
from .models import Media, Comment


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at')
    search_fields = ('title', 'description')
    list_filter = ('created_at',)
    ordering = ('-created_at',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'media', 'created_at')
    search_fields = ('author', 'text')
    list_filter = ('created_at',)
    raw_id_fields = ('media',)
    ordering = ('-created_at',)
