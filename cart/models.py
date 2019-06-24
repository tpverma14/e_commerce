from django.contrib.auth.models import User
from django.db import models

from django.utils.translation import gettext_lazy as _
from decimal import Decimal

from coupon.models import Coupon
from myshop.models import Product, Upload_images
from django.core.validators import MinValueValidator, MaxValueValidator

class Checkout(models.Model):
    country =models.CharField(_('country'),max_length=100,db_index=True)
    first_name = models.CharField(_('first_name'), max_length=50)
    last_name = models.CharField(_('last_name'), max_length=50)
    address = models.CharField(_('address'), max_length=250)
    email = models.ForeignKey(User,on_delete=models.CASCADE,related_name='emails')
    postal_code = models.CharField(_('postal_code'), max_length=20)
    city = models.CharField(_('city'), max_length=100)
    phone = models.IntegerField(default=0)
    other_notes = models.TextField(_('other_notes') ,max_length=500)
    paid = models.BooleanField(default=False)
    coupon=models.ForeignKey(Coupon,related_name='orders',on_delete=models.CASCADE,null=True, blank=True)
    discount=models.IntegerField(default=0,validators=[MinValueValidator(0),MaxValueValidator(80)],null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        total_cost = sum(item.get_cost() for item in self.items.all())
        return total_cost - total_cost*(self.discount/Decimal('100'))


class Oder_item(models.Model):
    order=models.ForeignKey(Checkout,related_name='items',on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE ,related_name='order_item')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def  get_cost(self):
        return self.price * self.quantity