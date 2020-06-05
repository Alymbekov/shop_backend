from rest_framework import serializers
from .models import Category
from rest_framework_recursive.fields import RecursiveField


class CategoryListSerializers(serializers.ModelSerializer):
    """Get list Categoty model"""
    children = RecursiveField(many=True) # return subcategory

    class Meta:
        model = Category
        fields = ('title', 'slug', 'children', 'parent')


class CategoryCreateSerializers(serializers.ModelSerializer):
    """Get list Categoty model"""

    class Meta:
        model = Category
        fields = ('title', 'slug', 'parent')
