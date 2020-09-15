from django.urls import path
from .views import Home, Products, ProductDetail

app_name = 'Store'

urlpatterns = [
    path('', Home, name='home'),
    path('Products/', Products, name='products'),
    path('Products/<int:id>', ProductDetail, name='details'),
]
