from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# post
class Post(models.Model):
    title = models.CharField('Название', max_length=250)
    content = models.TextField('Содержимое', blank=True)
    active = models.BooleanField(default=False, blank=True, null=True)
    date = models.DateField('Дата публикации', auto_now_add=True)
    slug = models.SlugField('url отметка', db_index=True, max_length=30, unique=True)
    like = models.PositiveIntegerField('Лайки', default=0, blank=True)
    dislike = models.PositiveIntegerField('Дизлайки', default=0, blank=True)
    author = models.ForeignKey(User, on_delete='PROTECT', related_name='postAuthor', verbose_name='Пользователь')
    views = models.PositiveIntegerField('Просмотры', default=True, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.slug)])

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Comments(models.Model):
    content = models.TextField('Содержимое', max_length=200)
    post = models.ForeignKey(Post, related_name='postComment', on_delete=models.CASCADE, verbose_name='Комментарий',
                             default=True)
    author = models.ForeignKey(User, on_delete='PROTECT', related_name='commentAuthor')
    date = models.DateTimeField('Опубликован', auto_now=True)
    like = models.PositiveIntegerField('Лайки', default=0, blank=True)
    views = models.PositiveIntegerField('Просмотры', default=0, blank=True)
    dislike = models.PositiveIntegerField('Дизлайки', default=0, blank=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'