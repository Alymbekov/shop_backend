from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
)
from .models import Category
from .serializers import CategoryListSerializers


class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializers


# class CategoryCreateView(CreateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategoryListSerializers
