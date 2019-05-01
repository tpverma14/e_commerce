from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Categories(models.Model):
    categories_name= models.CharField(db_index=True,max_length=100)
    slug= models.SlugField(max_length=100,unique=True,db_index=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Items(models.Model):
    categories=models.ForeignKey(Categories,related_name='categories')
    product_name=models.CharField(max_length=300)
    stock=models.IntegerField()
    price=models.IntegerField(validators=[MinValueValidator(100), MaxValueValidator(10000)])

    