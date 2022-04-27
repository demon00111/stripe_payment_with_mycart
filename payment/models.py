from email.mime import image
from pickle import TRUE
from unicodedata import name
from django.db import models

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100,null=TRUE)
    currency = models.CharField(max_length=100,null=TRUE)
    amount = models.CharField(max_length=100,null=TRUE)
    img = models.ImageField(null = TRUE)

    def __str__(self):
        return self.name


class Cart(models.Model):
    # product_id = models.ForeignKey(Products, null=True, on_delete=models.CASCADE)  # no change
    name = models.CharField(max_length=100,null=TRUE)
    quantity = models.CharField(max_length=100,null=TRUE)
    currency = models.CharField(max_length=100,null=TRUE)
    amount = models.CharField(max_length=100,null=TRUE)

    def __str__(self):
        return self.name