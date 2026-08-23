from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    author = models.CharField(max_length=100, verbose_name='Автор')
    genre = models.CharField(max_length=50, verbose_name='Жанр')
    year = models.IntegerField(verbose_name='Год издания')

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return self.title
