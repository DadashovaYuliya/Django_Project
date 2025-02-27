from django.db import models

class Blog(models.Model):
    name = models.CharField(max_length=150, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Содержимое')
    image = models.ImageField(upload_to='blog/image', verbose_name='Превью', blank=True, null=True)
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    is_publication = models.BooleanField(verbose_name='Признак публикации')
    counter = models.PositiveIntegerField(default=0, verbose_name='Количество просмотров')

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
        ordering = ['name']

    def __str__(self):
        return self.name
