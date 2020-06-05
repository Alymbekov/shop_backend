from django.db import models
from apps.categorys.models import Category


class Product(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to='product_images/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    salesPrice = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=False)
    stock = models.PositiveIntegerField(default=1)
    in_stock = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title


class Color(models.Model):
    pass


class Size(models.Model):
    pass


class ProductImages(models.Model):
    pass


class Meta(models.Model):
    pass


