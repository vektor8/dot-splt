from django.db import models

class User(models.Model):
    email = models.CharField(max_length = 256)
    full_name = models.CharField(max_length = 512)

class Product(model.Model):
    name = models.CharField(max_length=255)
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
    unit_price = models.IntegerField()
    quantity = models.IntegerField()

class Bill(models.Model):
    bill_token = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
