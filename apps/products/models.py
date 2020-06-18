from django.db import models
from apps.categorys.models import Category
from django.db.models.signals import pre_save
from shop.utils import slug_generator
from datetime import datetime
from django.utils.crypto import get_random_string

class Product(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='product_images\%Y\%m\%d/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    salesPrice = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=False)
    stock = models.PositiveIntegerField(default=1)
    in_stock = models.BooleanField(default=True)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            unique_name = get_random_string(length=32)
            date = datetime.now()
            self.image.name = f'{str(date)} {unique_name}.jpg'

        super().save(*args, **kwargs)

def product_slug_generate(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slug_generator(instance)

pre_save.connect(product_slug_generate, sender=Product)



class Color(models.Model):
    pass


class Size(models.Model):
    pass


class ProductImages(models.Model):
    pass


class Meta(models.Model):
    pass