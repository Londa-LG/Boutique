from django.db import models


class Categories(models.Model):
    title = models.CharField(max_length=50)
    thumbnail = models.ImageField()
    center = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Categories'


class Product(models.Model):
    thumbnail = models.ImageField()
    name = models.CharField(max_length=60)
    description = models.TextField()
    price = models.IntegerField()
    quantity = models.IntegerField()
    SKU = models.IntegerField()
    category = models.ManyToManyField(Categories)
    trending = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Product_images')

    def __str__(self):
        return self.product.name