from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from .models import Category
from .serializers import (
    CategorySerializers,
    CategoryUpdateSerializer,
    CategoryCreateSerializer,
    CategoryDeleteSerializer,
)
from django_filters.rest_framework import DjangoFilterBackend


class CategoryListView(ListAPIView):
    queryset = Category.objects.filter(parent=None)
    serializer_class = CategorySerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', ]


class CategoryCreateView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryCreateSerializer


class CategoryDetailView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class CategoryUpdateView(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryUpdateSerializer


class CategoryDeleteView(DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDeleteSerializer
