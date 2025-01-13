from django.db import models
from django.contrib.auth.models import User
from django.template import defaultfilters

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length = 255, verbose_name="Title")

    class Meta:
        ordering = ['title']

class Article(models.Model):
    title = models.CharField(max_length = 255, verbose_name="Title")
    slug = models.SlugField()
    article = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(default='default.png', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    class Meta:
        ordering = ['-created_at']


    def __str__(self):
        return self.title

    def created_date_formatted(self):
        return defaultfilters.date(self.created_at, "M d, Y")

    def snippet(self):
        return self.article[:50] + '...'