from django.db import models
from django.contrib.auth.models import User

from Store.models import Product


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_price = models.FloatField()
    complete = models.BooleanField()

    def __str__(self):
        return self.product.name

class BillingDetails(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    first_name = models.CharField(null=True, max_length=100)
    last_name = models.CharField(null=True, max_length=100)
    email = models.EmailField(null=True, max_length=100)
    phone_number = models.IntegerField(null=True,)
    company_name = models.CharField(null=True, max_length=100)
    country = models.CharField(null=True, max_length=100)
    address_line1 = models.CharField(null=True, max_length=100)
    address_line2 = models.CharField(null=True, max_length=100)
    town_or_city = models.CharField(null=True, max_length=100)
    state_or_country = models.CharField(null=True, max_length=100)

    class Meta:
        verbose_name_plural = 'Billing Details'

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    orders = models.ManyToManyField(Order)
    address = models.ForeignKey(BillingDetails, on_delete=models.CASCADE)
    coupon = models.CharField(max_length=40)
    order_total = models.FloatField()