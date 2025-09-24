import uuid
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    CATEGORY_CHOICES = [
        ('jersey', 'Jersey'),
        ('sepatu', 'Sepatu'),
        ('bola', 'Bola'),
        ('merchandise', 'Merchandise'),
        ('accessory', 'Accessory'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)           # nama item
    price = models.IntegerField()                     # harga item
    description = models.TextField()                  # deskripsi item
    thumbnail = models.URLField(blank=True, null=True) # URL gambar item
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='jersey')
    is_featured = models.BooleanField(default=False)  # status unggulan

    stock = models.PositiveIntegerField(default=0)       # stock / quantity
    brand = models.CharField(max_length=100, blank=True) # brand
    rating = models.FloatField(default=0.0)              # rating (aggregate)

    def __str__(self):
        return f"{self.name}"
