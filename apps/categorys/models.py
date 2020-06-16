from django.db import models
from shop.utils import slug_generator
from django.db.models.signals import pre_save


class Category(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='children')

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.title


def category_slug_generate(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slug_generator(instance)


pre_save.connect(category_slug_generate, sender=Category)
