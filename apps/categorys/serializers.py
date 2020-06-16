from rest_framework import serializers
from .models import Category


class RecursiveSerializer(serializers.Serializer):
    """Get recursive children"""

    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class CategoryListSerializers(serializers.ModelSerializer):
    """Get list Categoty model"""
    children = RecursiveSerializer(many=True)  # return subcategory

    class Meta:
        model = Category
        fields = ('title', 'slug', 'children', 'parent')


class CategoryCreateSerializers(serializers.ModelSerializer):
    """Get list Categoty model"""

    class Meta:
        model = Category
        fields = ('title', 'slug', 'parent')
