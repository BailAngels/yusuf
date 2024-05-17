from django.db import models


class Post(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name='Название',
    )
    description = models.TextField(
        verbose_name='Текст',
    )
    image = models.ImageField(
        upload_to='posts/',
        verbose_name='Изображение',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания',
    )

    
    def __str__(self):
        return self.title
    

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'