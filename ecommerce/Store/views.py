from django.shortcuts import render
from django.http import HttpResponse

from .models import Categories, Product

def Home(request):
    center = Categories.objects.filter(center=True)
    side = Categories.objects.filter(center=False)
    featured = Product.objects.filter(trending=True)
    context = {
        'center': center,
        'side': side,
        'featured': featured,
    }
    return render(request, 'Store/index.html', context)

def Products(request):
    return HttpResponse('<h1>This is the Store products page</h1>')

def ProductDetail(request,id):
    return HttpResponse('<h1>Here you get to know a little more about the product you clicked on')