from django.db import models
from django.contrib.auth.models import User
from main.models import Product
from django.utils import timezone

# Create your models here.

class Order(models.Model):
    number = models.CharField(max_length=64)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.number
