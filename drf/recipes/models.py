from django.db import models


class Tag(models.Model):
    name = models.CharField('Тег', max_length=255)
    slug = models.SlugField('Слаг', unique=True)

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'

    def __str__(self):
        return self.name
