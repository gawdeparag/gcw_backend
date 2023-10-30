from django.db import models

# Create your models here.
class Order(models.Model):
    order_id = models.IntegerField(auto_created=True, unique=True, null=False)  
    car_name = models.CharField(max_length=100, null=False)  
    car_brand = models.CharField(max_length=100, null=False) 
    car_model = models.CharField(max_length=100)
    service_name = models.CharField(max_length=100, null=False)
    service_cost = models.DecimalField(null=False, decimal_places=2, max_digits=7)
    add_ons = models.JSONField(list)
    is_done = models.BooleanField(default=False)
    total_cost = models.DecimalField(null=False, decimal_places=2, max_digits=7)
    created_by = models.CharField(null=True, max_length=20)
    created_at = models.DateTimeField(null=False, auto_now=True)
    updated_at = models.DateTimeField(null=False, auto_now_add=True)
    assigned_to = models.CharField(max_length=100)
    booked_for_date = models.DateTimeField(null=True)

    class Meta:
        db_table = "gcw_order"
