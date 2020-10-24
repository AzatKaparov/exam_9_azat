from django.db import models
from django.contrib.auth import get_user_model


class Photo(models.Model):
    img = models.ImageField(verbose_name='Картинка', null=False, blank=False)
    sign = models.CharField(verbose_name='Подпись', null=False, blank=False, max_length=100)
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    author = models.ForeignKey(get_user_model(), verbose_name='Автор', related_name='author', on_delete=models.CASCADE)
    favorites = models.ManyToManyField(get_user_model(), related_name='favorites', verbose_name='Избранное', blank=True)

    def __str__(self):
        return f'{self.author} | {self.sign[:20]}'

    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'

