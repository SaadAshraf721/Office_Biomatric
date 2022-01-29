from django.db import models

# Create your models here.
class categories(models.Model):

    name = models.CharField(max_length = 20)
    create_at = models.DateTimeField(auto_now=True)

class products(models.Model):
    categories = models.ForeignKey(categories, on_delete=models.CASCADE)
    name = models.CharField(max_length = 50)
    price = models.IntegerField()
    quantity = models.IntegerField()
    expiry = models.CharField(max_length = 50)
    profit = models.IntegerField()
    barcode = models.CharField(max_length = 50)
    create_at = models.DateTimeField(auto_now=True)

class update_product_price(models.Model):
    products = models.ForeignKey(products, on_delete=models.CASCADE)
    old_price = models.IntegerField()
    new_price = models.IntegerField()
    create_at = models.DateTimeField(auto_now=True)

class update_product_quantity(models.Model):
    products = models.ForeignKey(products, on_delete=models.CASCADE)
    new_quantity = models.IntegerField()
    old_quantity = models.IntegerField()
    create_at = models.DateTimeField(auto_now=True)


