from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Categories, Product, Subcategories, ProductImage
from Marketing.models import Emails
from Cart.models import Order, Cart

def Home(request):

    # Email form
    if request.method == "POST":
        email = request.POST['email']
        new_signup = Emails()
        new_signup.email = email
        new_signup.save()

    # Products and categories
    center = Categories.objects.filter(center=True, home=True)
    side = Categories.objects.filter(center=False, home=True)
    featured = Product.objects.filter(trending=True)

    context = {
        'center': center,
        'side': side,
        'featured': featured,
    }
    return render(request, 'Store/index.html', context)


def ProductsView(request):

    # Aside categories
    health_cat = Categories.objects.get(title="Health & Beauty")
    fashion_cat = Categories.objects.get(title="Fashion & Accessories")
    electronics_cat = Categories.objects.get(title="Electronics")
    health_sub = Subcategories.objects.filter(category=health_cat)
    electronics_sub = Subcategories.objects.filter(category=electronics_cat)
    fashion_sub = Subcategories.objects.filter(category=fashion_cat)

    # Pagination
    products_qs = Product.objects.all()
    paginator = Paginator(products_qs, 6)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginator_qs = paginator.page(page)
    except PageNotAnInteger:
        paginator_qs = paginator.page(1)
    except EmptyPage:
        paginator_qs = paginator.page(paginator.num_pages)

    context = {
        'products': products_qs,
        'page_var': page_request_var,
        'paginator': paginator_qs,
        'health': health_sub,
        'electronics': electronics_sub,
        'fashion': fashion_sub
    }
    return render(request, 'Store/shop.html', context)

def AddtoCartDetail(request,id):
    # Gathering all the order object elements
    product = Product.objects.get(id=id)
    price = product.price

    # Creating order object
    order = Order.objects.create(user=request.user, product=product, quantity=1, total_price=price, complete=False)

    # Assign order object to user Cart
    cart = Cart.objects.get(user=request.user)
    cart.orders.add(order)
    return redirect('Cart:cart')


def ProductDetail(request,id):
    # Products
    product_qs = Product.objects.filter(id=id)
    product = Product.objects.get(id=id)
    images = ProductImage.objects.filter(product=product)
    # Related products
    related_qs = Product.objects.filter(category=product.category)

    # Pagination
    paginator = Paginator(related_qs, 6)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginator_qs = paginator.page(page)
    except PageNotAnInteger:
        paginator_qs = paginator.page(1)
    except EmptyPage:
        paginator_qs = paginator.page(paginator.num_pages)

    context = {
        'product': product_qs,
        'images': images,
        'related': related_qs,
        'paginator': paginator_qs,
        'page_var': page_request_var
    }
    return render(request, 'Store/detail.html', context)


def SubCatSearch(request,id):
    # Aside subcategories
    health_cat = Categories.objects.get(title="Health & Beauty")
    fashion_cat = Categories.objects.get(title="Fashion & Accessories")
    electronics_cat = Categories.objects.get(title="Electronics")
    health_sub = Subcategories.objects.filter(category=health_cat)
    electronics_sub = Subcategories.objects.filter(category=electronics_cat)
    fashion_sub = Subcategories.objects.filter(category=fashion_cat)

    # Products list
    sub_cat = Subcategories.objects.get(id=id)
    products_qs = sub_cat.product_set.all()
    count = products_qs.count()

    # Pagination
    paginator = Paginator(products_qs, 6)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginator_qs = paginator.page(page)
    except PageNotAnInteger:
        paginator_qs = paginator.page(1)
    except EmptyPage:
        paginator_qs = paginator.page(paginator.num_pages)

    context = {
        'health': health_sub,
        'electronics': electronics_sub,
        'fashion': fashion_sub,
        'products': paginator_qs,
        'page_var': page_request_var,
        'count': count
    }
    return render(request, 'Store/search.html', context)

def CatSearch(request,id):
    # Aside subcategories
    health_cat = Categories.objects.get(title="Health & Beauty")
    fashion_cat = Categories.objects.get(title="Fashion & Accessories")
    electronics_cat = Categories.objects.get(title="Electronics")
    health_sub = Subcategories.objects.filter(category=health_cat)
    electronics_sub = Subcategories.objects.filter(category=electronics_cat)
    fashion_sub = Subcategories.objects.filter(category=fashion_cat)

    # Products list
    sub_cat = Categories.objects.get(id=id)
    products_qs = sub_cat.product_set.all()
    count = products_qs.count()

    # Pagination
    paginator = Paginator(products_qs, 6)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginator_qs = paginator.page(page)
    except PageNotAnInteger:
        paginator_qs = paginator.page(1)
    except EmptyPage:
        paginator_qs = paginator.page(paginator.num_pages)

    context = {
        'health': health_sub,
        'electronics': electronics_sub,
        'fashion': fashion_sub,
        'products': paginator_qs,
        'page_var': page_request_var,
        'count': count
    }
    return render(request, 'Store/search.html', context)