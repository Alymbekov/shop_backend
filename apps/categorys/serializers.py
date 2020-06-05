from rest_framework import serializers
from .models import Category


class RecursiveSerializer(serializers.Serializer):
    """Get children"""
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class CategorySerializers(serializers.ModelSerializer):
    """Get list Categoty model"""
    children = RecursiveSerializer(many=True)

    class Meta:
        model = Category
        fields = ('id', 'title', 'slug', 'parent', 'children')


class CategoryUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title', 'parent',)


class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class CategoryDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
