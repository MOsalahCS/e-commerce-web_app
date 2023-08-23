from .models import *
from rest_framework import serializers

class OrderItemSerializer(serializers.ModelSerializer):
    price = serializers.SerializerMethodField()
    cost = serializers.SerializerMethodField()

    class Meta:
        model=OrderItem
        fields='__all__'

    def get_price(self, obj):
        return obj.product.price
    
    def get_cost(self, obj):
        return obj.cost
        


class OrdersreadSerializer(serializers.ModelSerializer):

    buyer = serializers.CharField(source='buyer.get_full_name', read_only=True)
    order_items = OrderItemSerializer(read_only=True, many=True)
    total_cost = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model=Orders
        fields='__all__'


    def get_total_cost(self, obj):
        return obj.total_cost
    



class OrderswriteSerializer(serializers.ModelSerializer):

    client = serializers.HiddenField(default=serializers.CurrentUserDefault())
    order_items = OrderItemSerializer(many=True)

    class Meta:
        model = Orders
        fields='__all__'

    def create(self, validated_data):
        orders_data = validated_data.pop('order_items')
        order = Orders.objects.create(**validated_data)

        for order_data in orders_data:
            OrderItem.objects.create(order=order, **order_data)

        return order
    
   

