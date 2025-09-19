from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    """
    Serializer for the Order model to expose fields over the REST API.
    """

    class Meta:
        model = Order
        fields = [
            "id",
            "order_number",
            "customer_name",
            "status",
            "total_amount",
            "created_at",
            "delivered_at",
            "invoiced_at",
        ]
        read_only_fields = ["id", "created_at", "delivered_at", "invoiced_at"]
