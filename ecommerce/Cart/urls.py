from django.urls import path

from .views import CartView, BillingAdressView, AddToCart, DeletefromCart

app_name = 'Cart'

urlpatterns = [
    path('', CartView, name='cart'),
    path('AddtoCart/<int:id>/', AddToCart, name='add'),
    path('Address/', BillingAdressView, name='checkout'),
    path('Addtocart/Delete/<int:id>/', DeletefromCart, name='delete'),
]
