from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Order, Cart, BillingDetails
from Store.models import Product
from Marketing.models import CouponCode
from .forms import BillingForm

@login_required
def CartView(request):
    # variable
    total = 0

    # Collecting cart items
    order_qs = Order.objects.filter(user=request.user)

    # Total price before coupon
    for orders in order_qs:
        total = total + orders.total_price

    context = {
        'orders': order_qs,
        'Total': total
    }
    return render(request, 'Cart/cart.html', context)

@login_required
def BillingAdressView(request):
    # Variable
    total = 0

    # Collect orders
    orders_qs = Order.objects.filter(user=request.user)

    # Calculate cart total
    for orders in orders_qs:
        total = total + orders.total_price

    # Form handling
    if request.method == "POST":
        form = BillingForm(request.POST or None)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('first_name')
            billing = BillingDetails.objects.filter(first_name=name)
            billing.update(user=request.user)
            return redirect('Store:home')
        else:
            for msg in form.error_messages:
                messages.error(request, f'{msg}:{form.error_messages[msg]}')

    # Form
    form = BillingForm()

    context = {
        'Total': total,
        'Orders': orders_qs,
        'form': form
    }
    return render(request, 'Cart/checkout.html', context)

@login_required
def AddToCart(request,id):
    # Gathering all the order object elements
    product = Product.objects.get(id=id)
    price = product.price

    # Creating order object
    order = Order.objects.create(user=request.user, product=product, quantity=1, total_price=price, complete=False)

    # Assign order object to user Cart
    cart = Cart.objects.get(user=request.user)
    cart.orders.add(order)
    return redirect('Cart:cart')

def DeletefromCart(request,id):
    # Gather order object
    order = Order.objects.get(id=id)

    # Delete object
    order.delete()
    return redirect('Cart:cart')