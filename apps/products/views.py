from rest_framework.generics import (
    ListCreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, CreateAPIView
)
from .serializers import ProductListSerializer, ProductSerializer
from .models import Product
from django_filters.rest_framework import DjangoFilterBackend


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', ]


class ProductDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductCreateView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# class ProductUpdateView(UpdateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductListSerializer
