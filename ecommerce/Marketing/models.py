from django.db import models

class Emails(models.Model):
    email = models.CharField(max_length=100)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = 'Emails'

class CouponCode(models.Model):
    coupon_code = models.CharField(max_length=100)
    timestamp = models.DateField(auto_now_add=True)
    discount_percentage = models.IntegerField(default=0)
