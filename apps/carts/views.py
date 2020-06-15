from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework import status
from .models import Cart, CartItem
from .serializers import CartItemSerializers, CartSerializers
from rest_framework.response import Response
from apps.products.models import Product


class CartDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializers

    def retrieve(self, request, *args, **kwargs):
        queryset = Cart.objects.get_or_new(request)
        serializer = CartSerializers(queryset, context={'request': request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class CartItemView(CreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializers

    def post(self, request, *args, **kwargs):
        cart = Cart.objects.get_or_new(request)
        cartitem = cart.cart_items.all()
        product_item = Product.objects.get(pk=request.data['product_item'])
        for item in cartitem:
            if item.product_item == product_item:
                return Response(data={'message': 'The product is already in the cart'},
                                status=status.HTTP_400_BAD_REQUEST)
            if product_item.stock == 0 or int(request.data['amount']) > product_item.stock:
                return Response(data={'message': 'No enough stock'}, status=status.HTTP_400_BAD_REQUEST)
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        cart = Cart.objects.get_or_new(self.request)
        serializer.save(cart=cart)

