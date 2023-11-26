from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'car_name', 
            'car_brand', 
            'car_model', 
            'service_name', 
            'service_cost',
            'add_ons',
            'is_done',
            'total_cost',
            'created_by',
            'created_at',
            'updated_at',
            'assigned_to',
            'booked_for_date',
            ]
