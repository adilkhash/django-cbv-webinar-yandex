from django.contrib import admin

from news.models import News, Comment


class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'slug', 'created']
    ordering = ('-created',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'news', 'text', 'created']
    ordering = ('-created',)


admin.site.register(News, NewsAdmin)
admin.site.register(Comment, CommentAdmin)
