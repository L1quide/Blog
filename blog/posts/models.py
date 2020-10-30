from django.db import models
from django.urls import reverse
from django.utils import timezone

class Post(models.Model):
    title = models.CharField('Заголовок',max_length=300)
    slug = models.SlugField(max_length=160, unique=True, blank=True, null=True)
    content = models.TextField('Основной контент')
    image = models.ImageField('Изображение', upload_to='media/',  blank=True, null=True)
    date = models.DateTimeField(default=timezone.now)
    autor = models.SlugField("Автор", max_length=200)
    publick = models.BooleanField("Активность", default=False)
    archive = models.BooleanField("Архив", default=False)

    def get_absolute_url(self):
        return reverse('content', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


