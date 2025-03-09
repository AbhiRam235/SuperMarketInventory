from django.db import models
from users.models import User
# Create your models here.
class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('packed', 'Packed'),
        ('assigned_for_delivery', 'Assigned for Delivery'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ]
    
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    delivery_price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    order_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    delivery_location = models.CharField(max_length=255)
    
    def __str__(self):
        return f"Order {self.id} - {self.customer.name}"
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    order_items = models.JSONField(default=list)  # Stores [{'product_id': 1, 'quantity': 2, 'price': 100.00}]

    def __str__(self):
        return f"Items for Order {self.order.id}"
    
class Cart(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    cart_items = models.JSONField(default=list)  # Stores [{'product_id': 1, 'quantity': 2, 'price': 100.00}]

    def __str__(self):
        return f"Cart - {self.customer.name}"
