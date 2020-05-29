from rest_framework import serializers
from .models import Category


class CategoryListSerializers(serializers.ModelSerializer):
    """Get list Categoty model"""

    class Meta:
        model = Category
        fields = '__all__'
