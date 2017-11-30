from django.db import models
from . import Category
from django.template.defaultfilters import slugify

class Font(models.Model):
    category = models.ForeignKey(Category)
    name = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self,*args, **kwargs): # For Python 2, use __unicode__ too
        self.slug = slugify(self.name)
        super(Font, self).save(*args, **kwargs)

    def __str__(self):
        return self.name