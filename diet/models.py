from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=32)
    describe = models.TextField(max_length=None)
    calories = models.DecimalField(decimal_places=2, max_digits=8)
    image = models.ImageField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    available = models.BooleanField(default=True)


class Categories(models.Model):
    name = models.CharField(max_length=32)
    products = models.ManyToManyField(Product)