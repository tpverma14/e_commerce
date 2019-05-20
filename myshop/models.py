from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Category(models.Model):
    categories_name = models.CharField(db_index=True, max_length=100)
    slug = models.SlugField(max_length=100, unique=True, db_index=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.categories_name

    @property
    def get_absolute_url(self):
        return "%s" % (self.slug)

class Category_banner(models.Model):
    category_banner=models.ForeignKey(Category,related_name='category_image',on_delete=models.CASCADE)
    category_image=models.ImageField(upload_to='product_banner',blank=False)

class Sub_Category(models.Model):
    categories = models.ForeignKey(Category, related_name='categories', on_delete=models.CASCADE)
    product_name = models.CharField(max_length=300)
    slug = models.SlugField(max_length=100)
    stock = models.IntegerField()

    def __str__(self):
        return self.product_name


class Product(models.Model):
    product_id = models.ForeignKey(Sub_Category, related_name='product', on_delete=models.CASCADE)
    brand_name = models.CharField(max_length=100)
    price = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10000)])
    description = models.TextField(max_length=500)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.brand_name


class Upload_images(models.Model):
    image_id = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products_image', blank=False)



class Size_quantity(models.Model):
    CATEGORIES_CHOICES = (
        ('XS', 'Extra Small'),
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large')
    )
    product = models.ForeignKey(Product, related_name='sizes', on_delete=models.CASCADE)
    size = models.CharField(choices=CATEGORIES_CHOICES, null=True, max_length=100)
    quantity = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100000)], null=True)


class Banner(models.Model):
    name = models.CharField(max_length=32, blank=False)
    discount = models.IntegerField(blank=False)
    valid_from = models.DateTimeField(blank=False)
    valid_to = models.DateTimeField(blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField()

    # @property
    # def get_active_banners(self):
    #     return Banner.objects.filter(active=True)

    def __str__(self):
        return self.name


class Upload_data(models.Model):
    banner = models.ForeignKey(Banner, related_name='banner', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='background_image', blank=False)
