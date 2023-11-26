from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Order
from .serializers import OrderSerializer

class OrderAPIView():
    @api_view(['GET'])
    def get_orders(self):
        orders = Order.objects.all()
        order_serializer = OrderSerializer(orders, many=True)
        if orders.exists():
            return Response(order_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(order_serializer.data, status=status.HTTP_204_NO_CONTENT)

    @api_view(['POST'])
    def create_order(request):
        order_serializer = OrderSerializer(data=request.data)
        if order_serializer.is_valid():
            order_serializer.save()
            return Response(order_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(order_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    @api_view(['GET', 'PUT', 'DELETE'])
    def order(request, id, format=None):
        try:
            order = Order.objects.get(pk=id)
        except Order.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        if request.method == "GET":
            order_serializer = OrderSerializer(order)
            return Response(order_serializer.data)
        elif request.method == "PUT":
            order_serializer = OrderSerializer(order, data=request.data)
            if order_serializer.is_valid():
                order_serializer.update(order, order_serializer)
                return Response(order_serializer.data)
            return Response(order_serializer.errors, status=status.HTTP_400_BAD_REQUEST)