from django.urls import path
from .views import Home, ProductsView, ProductDetail, SubCatSearch, CatSearch

app_name = 'Store'

urlpatterns = [
    path('', Home, name='home'),
    path('Products/', ProductsView, name='products'),
    path('Products/<int:id>', ProductDetail, name='details'),
    path('Products/Search/<int:id>/', SubCatSearch, name='search'),
    path('Products/Category/Search/<int:id>/', CatSearch, name='catsearch')
]
