from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Order
from Store.models import Product


def CartView(request):
    # variable
    total = 0

    # Collecting cart items
    order_qs = Order.objects.all()

    # Total price before coupon
    for orders in order_qs:
        total = total + orders.total_price

    context = {
        'orders': order_qs,
        'Total': total
    }
    return render(request, 'Cart/cart.html', context)

def BillingAdressView(request):
    return render(request, 'Cart/checkout.html')

def AddToCart(request,id ):
    # Gathering all the order object elements
    product = Product.objects.get(id=id)
    price = product.price

    # Creating order object
    Order.objects.create(product=product, quantity=1, total_price=price, complete=False)
    return redirect('Cart:cart')

