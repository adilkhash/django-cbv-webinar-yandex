from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import Truncator

User = get_user_model()


class News(models.Model):
    title = models.CharField(max_length=256, verbose_name='Заголовок')
    slug = models.SlugField(max_length=128, verbose_name='URL')
    text = models.TextField(verbose_name='Новость')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    author = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-created',)
        verbose_name = 'новость'
        verbose_name_plural = 'Новости'


class Comment(models.Model):
    text = models.TextField(verbose_name='Комментарий')
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return Truncator(self.text).words(10)

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ('-created',)
