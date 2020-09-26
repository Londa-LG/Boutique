from django.urls import path

from .views import CartView, BillingAdressView, AddToCart

app_name = 'Cart'

urlpatterns = [
    path('', CartView, name='cart'),
    path('Address/', BillingAdressView, name='checkout'),
    path('AddtoCart/<int:id>/', AddToCart, name='add'),
]
