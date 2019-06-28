from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Count


class Category(models.Model):
    categories_name = models.CharField(db_index=True, max_length=100)
    slug = models.SlugField(max_length=100, unique=True, db_index=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.categories_name


class Category_banner(models.Model):
    category_banner=models.ForeignKey(Category,related_name='category_image',on_delete=models.CASCADE)
    category_image=models.ImageField(upload_to='product_banner',blank=False)

class Sub_Category(models.Model):
    categories = models.ForeignKey(Category, related_name='categories', on_delete=models.CASCADE)
    product_name = models.CharField(max_length=300)
    featured_department=models.BooleanField()
    slug = models.SlugField(max_length=100)


    def __str__(self):
        return self.product_name

    @property
    def get_absolute_url_sub(self):
        return "/subcategory/%s/" % (self.slug)


class Product(models.Model):
    product_id = models.ForeignKey(Sub_Category, related_name='product_id', on_delete=models.CASCADE)
    brand_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    title = models.CharField(max_length=100)
    price = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10000)])
    discount=models.IntegerField(blank=True,null=True)
    description = models.TextField(max_length=5000)
    additional_description = models.TextField(max_length=5000)
    feature_product=models.BooleanField()
    like = models.ManyToManyField(User, blank=True, related_name='product_like')
    available = models.BooleanField(default=True)


    def __str__(self):
        return self.brand_name


    @property
    def discount_price(self):
        if self.discount:
             sub_total = (self.discount * self.price) / 100
             total_price = self.price - sub_total
             return total_price
        return 0
    #
    # sub=[]
    #
    # def total_stock(self):
    #     for item in self.sizes.all():
    #         self.sub.append(item.size)
    #         sum=0
    #         leno=len(self.sub)
    #         for i in range(leno):
    #             sum=item.quantity+sum
    #     return sum


    @property
    def get_absolute_url(self):
        return "/product_detail/%s/" %(self.slug)


class Upload_images(models.Model):
    image_id = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products_image', blank=False)


class Size_quantity(models.Model):
    CATEGORIES_CHOICES = (
        ('GN','General '),
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
    discount = models.IntegerField(blank=True,null=True)
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


class Profile(models.Model):
    user=models.OneToOneField(User,related_name="user", on_delete=models.CASCADE)
    mobile_number=models.IntegerField(unique=True)

