import uuid
from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    CATEGORY_CHOICES = [
        ('shoes', 'Shoes'),
        ('equipment', 'Equipment'),
        ('uniform', 'Uniform'),
        ('t-shirt', 'T-Shirt'),
        ('socks', 'Socks'),
        ('merchandise', 'Merchandise'),
        ('other', 'Other'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')
    is_featured = models.BooleanField(default=False)
    stock = models.PositiveIntegerField(default=0)
    rating = models.FloatField(default=0)
    brand = models.CharField(max_length=255)


    def __str__(self):
        return self.name

    @property
    def is_stock_available(self):
        return self.stock > 0
'''
class Car(models.Model):
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    stock = models.IntegerField()
'''