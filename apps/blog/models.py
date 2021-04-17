from django.db import models
from apps.core.behaviours import *
from apps.categories.models import Categories

# Create your models here.


class Blog(CreateMixin, models.Model):
    categories = models.ForeignKey('categories.Categories', models.DO_NOTHING, null=True, blank=True, related_name="blog_categories")
    title = models.CharField(max_length=255, null=True, blank=True)
    slug = models.SlugField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='blogs/', null=True, blank=True)
    short_desc = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    live = models.BooleanField(default=False)

    class Meta:
        managed = True
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'

    def __str__(self):
        return self.title