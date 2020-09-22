from django.contrib import admin
from .models import Categories, Product, ProductImage, Subcategories

admin.site.register(Categories)
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Subcategories)

