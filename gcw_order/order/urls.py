from django.urls import path

from . import views


urlpatterns = [
    path("all", views.OrderAPIView.get_orders),
    path("create", views.OrderAPIView.create_order),
    path("<int:id>", views.OrderAPIView.order),
    path("update/<int:id>", views.OrderAPIView.order)
]