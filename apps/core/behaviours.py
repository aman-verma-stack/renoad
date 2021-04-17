from django.db import models


class CreateMixin(models.Model):
    created_on = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_on = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        abstract = True


class UserMixin(models.Model):
    name = models.CharField(max_length=120, null=True, blank=True)
    email = models.EmailField(max_length=120, null=True, blank=True)
    number = models.CharField(max_length=120, null=True, blank=True)
    
    class Meta:
        abstract = True


class SEOMixin(models.Model):
    seo_title = models.CharField(max_length=255)
    seo_keyword = models.CharField(max_length=255, null=True, blank=True)
    seo_description = models.CharField(max_length=255, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_on = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        abstract = True