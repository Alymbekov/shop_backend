from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
    RetrieveUpdateDestroyAPIView
)
from rest_framework import permissions
from .models import Category
from .serializers import CategoryListSerializers, CategoryCreateSerializers


class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializers


class CategoryCreateView(CreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Category.objects.all()
    serializer_class = CategoryCreateSerializers


class CategoryDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticatedOrReadOnly]
    serializer_class = CategoryListSerializers

# class CategoryDestroyView(DestroyAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategoryListSerializers


# class CategoryUpdateView(UpdateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategoryCreateSerializers
