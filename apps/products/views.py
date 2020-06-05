from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from .serializers import ProductListSerializer, ProductSerializer
from .models import Product


class ProdictListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    

class ProductDetailView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

#class ProductCreateView(CreateAPIView):
#   queryset = Product.objects.all()
#   serializer_class = ProductSerializer



