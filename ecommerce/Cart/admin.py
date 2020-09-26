from django.contrib import admin

from .models import Order, BillingDetails, Cart

admin.site.register(Order)
admin.site.register(BillingDetails)
admin.site.register(Cart)

