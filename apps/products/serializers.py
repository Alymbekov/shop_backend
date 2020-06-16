from rest_framework import serializers
from .models import Product


class ProductListSerializer(serializers.ModelSerializer):
    categories = serializers.StringRelatedField()

    class Meta:
        model = Product
        fields = ('title', 'description', 'image', 'price', 'categories')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"