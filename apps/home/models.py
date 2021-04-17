from django.db import models
from apps.core.behaviours import CreateMixin, SEOMixin
from ckeditor.fields import RichTextField


class HomeContent(SEOMixin, models.Model):
    description = models.TextField(null=True, blank=True)

    class Meta:
        managed = True
        verbose_name = 'Home Content'
        verbose_name_plural = 'Home Content'

    def __str__(self):
        return self.description



class Reviews(CreateMixin, models.Model):
    choices = (
        (0, 'Not Live'),
        (1, 'Live'),
    )
    stars = (
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5),
    )
    title = models.CharField(max_length=255, null=True, blank=True)
    description = RichTextField(null=True, blank=True)
    review_by = models.CharField(max_length=255, null=True, blank=True)
    live = models.IntegerField(default=0, choices=choices)
    rating = models.IntegerField(default=0, choices=stars)
    home = models.ForeignKey('HomeContent', models.DO_NOTHING,related_name="reviews_all")


    class Meta:
        managed = True
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'

    def __str__(self):
        return self.title



class Partners(CreateMixin, models.Model):
    image = models.ImageField(upload_to='partners/', null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)
    alt = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        managed = True
        verbose_name = 'Patner'
        verbose_name_plural = 'Patners'
    
    
    def __str__(self):
        return self.alt
    