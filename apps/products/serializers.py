from rest_framework import serializers
from .models import Product


class ProductListSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()

    class Meta:
        model = Product
        fields = ('id', 'title', 'description', 'image', 'price', 'category')
        

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class ProductUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('title', 'description', 'image', 'price',)
