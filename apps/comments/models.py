from django.db import models

from apps.posts.models import Post


class Comment(models.Model):
    text = models.TextField(
        verbose_name='текст'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='дата создания',
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name = 'comments'
    )
    parent = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='родитель'
    )

    def __str__(self):
        return self.text