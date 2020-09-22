from django.db import models
from django.urls import reverse

class Categories(models.Model):
    title = models.CharField(max_length=50)
    thumbnail = models.ImageField(upload_to='Categories')
    center = models.BooleanField(default=False)
    home = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Categories'

    def get_absolute_url(self):
        return reverse('Store:catsearch', kwargs={'id': self.id})


class Subcategories(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Subcategories'

    def get_absolute_url(self):
        return reverse('Store:search', kwargs={'id': self.id})

class Product(models.Model):
    thumbnail = models.ImageField(upload_to='Product_thumbnail')
    name = models.CharField(max_length=60)
    description = models.TextField()
    specifications = models.TextField(default='Product Specs')
    price = models.IntegerField()
    quantity = models.IntegerField()
    SKU = models.IntegerField()
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True, blank=True)
    subcategory = models.ManyToManyField(Subcategories)
    trending = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('Store:details', kwargs={'id': self.id})


class ProductImage(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Product_images')

    def __str__(self):
        return self.product.name