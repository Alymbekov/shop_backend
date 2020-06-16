from rest_framework import serializers
from .models import Order, Delivery


class OrderSerializers(serializers.HyperlinkedModelSerializer):
    """Get Order List"""

    class Meta:
        model = Order
        fields = (
            'url', 'user', 'first_name',
            'last_name', 'email', 'order_id',
            'created', 'total',
        )
        read_only_fields =  (
            'user', 'total', 'order_id',
            'created',
        )


class DeliverySerializer(serializers.HyperlinkedModelSerializer):
    """Get Delivery List"""

    class Meta:
        model = Delivery
        fields = ('name',)
