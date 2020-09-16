from django.db import models


# Create your models here.

class ProductsCategory(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        unique_together = ['name']

class Products(models.Model):
    category = models.ForeignKey(ProductsCategory, related_name='ctgory', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    count = models.IntegerField()
