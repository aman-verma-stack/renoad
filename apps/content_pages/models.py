from django.db import models
from apps.core.behaviours import CreateMixin, SEOMixin
from ckeditor.fields import RichTextField


class Cancellation(CreateMixin, models.Model):
    description = RichTextField(null=True, blank=True)

    class Meta:
        managed = True
        verbose_name = 'Canellation Policy'
        verbose_name_plural = 'Canellation Policy'


class Career(CreateMixin, models.Model):
    description = RichTextField(null=True, blank=True)

    class Meta:
        managed = True
        verbose_name = 'Career'
        verbose_name_plural = 'Career'


class Book(CreateMixin, models.Model):
    description = RichTextField(null=True, blank=True)

    class Meta:
        managed = True
        verbose_name = 'How To Book'
        verbose_name_plural = 'How To Book'


class Privacy(CreateMixin, models.Model):
    description = RichTextField(null=True, blank=True)

    class Meta:
        managed = True
        verbose_name = 'Privacy Policy'
        verbose_name_plural = 'Privacy Policy'


class Terms(CreateMixin, models.Model):
    description = RichTextField(null=True, blank=True)

    class Meta:
        managed = True
        verbose_name = 'Terms & Conditions'
        verbose_name_plural = 'Terms & Conditions'


class About(CreateMixin, models.Model):
    description = RichTextField(null=True, blank=True)

    class Meta:
        managed = True
        verbose_name = 'About'
        verbose_name_plural = 'About'


class Epapers(CreateMixin, models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to = 'e_papers/', null=True, blank=True)
    link = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        managed = True
        verbose_name = 'E-Paper'
        verbose_name_plural = 'E-Papers'


class Feedback(CreateMixin, models.Model):
    description = RichTextField(null=True, blank=True)

    class Meta:
        managed = True
        verbose_name = 'Feedback'
        verbose_name_plural = 'Feedback'
