from django.db import models
from apps.core.behaviours import CreateMixin

# Create your models here.

class Categories(CreateMixin, models.Model):
    choices = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8),
        (9, 9),
        (10, 10),
        (11, 11),
        (12, 12),
        (13, 13),
        (14, 14),
        (15, 15),
        (16, 16),
        (17, 17),
        (18, 18),
        (19, 19),
    )
    category = models.CharField(max_length=150, null=True, blank=True)
    category_image = models.ImageField(upload_to='category',null=True, blank=True)
    priority = models.IntegerField(default=0,choices=choices)
    slug = models.SlugField(null=True, blank=True, max_length = 250)
    live = models.BooleanField(default=False)

    def __str__(self):
        return self.category

    class Meta:
        managed = True
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'



class SubCategory(CreateMixin, models.Model):
    category = models.ForeignKey('Categories', models.DO_NOTHING, null=True, blank=True)
    name = models.CharField(max_length=250, null=True, blank=True)
    image = models.ImageField(upload_to='subcategory',null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)
    live = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name

    class Meta:
        managed = True
        verbose_name = 'Sub Category'
        verbose_name_plural = 'Sub Categories'