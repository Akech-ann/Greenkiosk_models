from django.db import models
from inventory.models import Product

class Cart(models.Model):
    products = models.ManyToManyField(Product)
    name = models.CharField(max_length=32)
    total = models.FloatField()
    image = models.ImageField(upload_to="images/")
    number_of_products = models.PositiveIntegerField()
    shipping_cost = models.FloatField()
    payment_options = models.CharField(max_length=20)
    discount = models.FloatField()

    def __str__(self):
        return self.name







