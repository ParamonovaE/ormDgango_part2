from django.core.exceptions import ValidationError
from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название тега')

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name
class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    tags = models.ManyToManyField(Tag, through='Scope')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title



class Scope(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scopes')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='scopes')
    is_main = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Тематики раздела'
        unique_together = ('article', 'tag')

    def save(self, *args, **kwargs):
        if self.is_main:
            # Проверяем, есть ли уже основной раздел для данной статьи
            main_scope = Scope.objects.filter(article=self.article, is_main=True).exclude(pk=self.pk)
            if main_scope.exists():
                raise ValidationError('Основным может быть только один раздел.')
        super().save(*args, **kwargs)
