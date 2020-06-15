from rest_framework.generics import ListCreateAPIView
from .models import Order, Delivery
from .selializers import OrderSerializers, DeliverySerializer


class OrderListCreateView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializers

    # def perform_create(self, serializer):
    #     user = self.request.user
    #     summa = 0

