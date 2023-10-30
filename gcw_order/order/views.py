from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Order
from .serializers import OrderSerializer

@api_view(['GET'])
def get_orders():
    orders = Order.objects.all()
    order_serializer = OrderSerializer(orders, many=True)
    return JsonResponse({order_serializer.data})

@api_view(['POST'])
def create_order(request):
    print(request)
    order_serializer = OrderSerializer(data=request.data)
    if order_serializer.is_valid():
        order_serializer.save()
        return Response(order_serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(order_serializer.errors, status=status.HTTP_400_BAD_REQUEST)