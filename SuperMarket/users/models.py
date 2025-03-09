from django.db import models

# Create your models here.
class User(models.Model):
    ROLE_CHOICES = [
        ('customer', 'Customer'),
        ('owner', 'Owner'),
        ('staff', 'Staff'),
        ('delivery', 'Delivery'),
    ]
    
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    phone = models.CharField(max_length=15, blank=True, null=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    locations = models.JSONField(default=list)  # Stores multiple locations for customers
    
    def __str__(self):
        return self.name