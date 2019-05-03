from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Categorie(models.Model):
    categories_name= models.CharField(db_index=True,max_length=100)
    slug= models.SlugField(max_length=100,unique=True,db_index=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def  __str__(self):
        return self.categories_name



class Sub_Categorie(models.Model):

    categories=models.ForeignKey(Categorie,related_name='categories',on_delete=models.CASCADE)
    product_name=models.CharField(max_length=300)
    slug = models.SlugField(max_length=100)
    stock=models.IntegerField()
    price=models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10000)])

    def __str__(self):
        return  self.product_name


class Product(models.Model):
    product_id=models.ForeignKey(Sub_Categorie,related_name='product',on_delete=models.CASCADE)
    brand_name = models.CharField(max_length=100)
    description=models.TextField(max_length=500)
    available=models.BooleanField(default=True)


    def __str__(self):
        return self.brand_name


class Upload_images(models.Model):

    image_id=models.ForeignKey(Product,related_name='images',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/products_image')





class Size_quantity(models.Model):
    CATEGORIES_CHOICES = (
        ('XS', 'Extra Small'),
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large')
    )
    product=models.ForeignKey(Product,related_name='sizes',on_delete=models.CASCADE)
    size = models.CharField(choices=CATEGORIES_CHOICES, null=True,max_length=100)
    quantity=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(100000)],null=True)
