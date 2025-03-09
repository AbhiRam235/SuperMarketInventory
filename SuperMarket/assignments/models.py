from django.db import models
from users.models import User
from orders.models import Order
# Create your models here.
class Assignment(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('packed', 'Packed'),
    ]
    
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    staff = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    packed_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    
    def __str__(self):
        return f"Assignment for Order {self.order.id}"