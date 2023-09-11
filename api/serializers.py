from rest_framework import serializers
from customer_management.models import Customer
from order_management.models import Order

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"





class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"