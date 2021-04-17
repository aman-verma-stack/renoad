from django.db import models
from apps.core.behaviours import CreateMixin

# Create your models here.

class City(CreateMixin, models.Model):
    city = models.CharField(max_length=200, null=True)
    slug = models.SlugField(null=True)
    
    def __str__(self):
        return self.city

    class Meta:
        managed = True
        verbose_name = 'City'
        verbose_name_plural = 'City'


class Language(CreateMixin, models.Model):
    language = models.CharField(max_length=100, null=True)
    slug = models.SlugField(null=True)

    def __str__(self):
        return self.language


    class Meta:
        managed = True
        verbose_name = 'Language'
        verbose_name_plural = 'Language'


class AdType(CreateMixin, models.Model):
    adtype = models.CharField(max_length=200, null=True)
    slug = models.SlugField()

    def __str__(self):
        return self.adtype

    class Meta:
        managed = True
        verbose_name = 'Ad Type'
        verbose_name_plural = 'Ad Type'