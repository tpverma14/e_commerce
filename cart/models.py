from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from decimal import Decimal
from myshop.models import Product


class Checkout(models.Model):
    country =models.CharField(max_length=100,db_index=True)
    first_name = models.CharField(_('first_name'), max_length=50)
    last_name = models.CharField(_('last_name'), max_length=50)
    address = models.CharField(_('address'), max_length=250)
    email = models.EmailField(_('email'), )
    postal_code = models.CharField(_('postal_code'), max_length=20)
    city = models.CharField(_('city'), max_length=100)
    phone = models.IntegerField(default=0)
    other_notes = models.TextField(max_length=500)
    paid = models.BooleanField(default=False)
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
    order=models.ForeignKey(Checkout,related_name='order',on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE ,related_name='items')
    quantity=models.TextField()
    price=models.TextField()

    def __str__(self):
        return '{}'.format(self.id)

    def  get_cost(self):
        return self.price * self.quantity