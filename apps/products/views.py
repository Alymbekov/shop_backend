from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAdminUser
from .serializers import ProductListSerializer, ProductSerializer, ProductUpdateSerializer
from .models import Product
from django_filters.rest_framework import DjangoFilterBackend


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'category', ]


class ProductDetailView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductCreateView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]


class ProductUpdateView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductUpdateSerializer
    permission_classes = [IsAdminUser]


class ProductDeleteView(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]

