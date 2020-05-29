from django.db import models
from apps.categorys.models import Category


class Product(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name


class ProductItem(models.Model):
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product.name}'s item"


class ProductItemImage(models.Model):
    image = models.ImageField(upload_to='product_img')
    product_item = models.ForeignKey(ProductItem, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product_item.product.name}'s image"
