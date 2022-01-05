import uuid
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50)

class Bill(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(User, on_delete=models.RESTRICT)

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    quantity = models.FloatField() 
    is_countable = models.BooleanField()
    bill_id = models.ForeignKey(Bill, on_delete=models.RESTRICT)

class Payments(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.RESTRICT)
    product_id = models.ForeignKey(Product, on_delete=models.RESTRICT)
    quantity = models.FloatField()
