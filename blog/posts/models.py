from django.db import models

class Post(models.Model):
    title = models.CharField(max_length='300')
    slug = models.SlugField(max_length='100', unique=True)
    content = models.TextField()
    date = models.DateTimeField()
    autor = models.SlugField(max_length='200')
    publick = models.BooleanField(default=False)


