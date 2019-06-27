from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.db import models

from django.utils.translation import gettext_lazy as _
from decimal import Decimal

from coupon.models import Coupon
from myshop.models import Product
from django.core.validators import MinValueValidator, MaxValueValidator




class Checkout(models.Model):
    checkout_id=models.ForeignKey(User,on_delete=models.CASCADE,related_name='emails')
    country =models.CharField(_('country'),max_length=100,db_index=True)
    first_name = models.CharField(_('first_name'), max_length=50)
    last_name = models.CharField(_('last_name'), max_length=50)
    address = models.CharField(_('address'), max_length=250)
    email = models.EmailField(_('email'),max_length=100)
    postal_code = models.CharField(_('postal_code'), max_length=20)
    city = models.CharField(_('city'), max_length=100)
    phone = models.IntegerField(default=0)
    paid = models.BooleanField(default=False)
    other_notes = models.TextField(_('other_notes') ,max_length=500)
    coupon=models.ForeignKey(Coupon,related_name='orders',on_delete=models.CASCADE,null=True, blank=True)
    discount=models.IntegerField(default=0,validators=[MinValueValidator(0),MaxValueValidator(80)],null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # def save(self,*args,**kwargs):
    #
    #
    #     try:
    #         Order_updates(self)
    #         obj = Order_updates.objects.get(order_id=self.id)
    #         super(Order_updates, obj).save(*args, **kwargs)
    #         print(obj.get_update(),"django")
    #         print(obj.__dict__)
    #         if obj.active == True and obj.update_desc == "Delivered":
    #             self.paid=True
    #         else:
    #             self.paid=False
    #     except ObjectDoesNotExist:
    #         pass
    #     super(Checkout, self).save(*args, **kwargs)

    def mysave(self):
        print("hello")
        self.paid =True
        self.save()

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        total_cost = sum(item.get_cost() for item in self.items.all())
        return total_cost - total_cost*(self.discount/Decimal('100'))







class Oder_item(models.Model    ):

    order=models.ForeignKey(Checkout,related_name='items',on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE ,related_name='order_item')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return '{}'.format(self.id)

    def  get_cost(self):
        return self.price * self.quantity


class Order_updates(models.Model):
    CATEGORIES_CHOICES = (
        ('Accepted','Accepted'),
        ('Packed','Packed'),
        ('Dispatched','Dispatched'),
        ('Delivered','Delivered'),
    )
    update_id=models.AutoField(primary_key=True)
    order_id=models.OneToOneField(Checkout,related_name='order_id',on_delete=models.CASCADE)
    update_desc =models.CharField(choices=CATEGORIES_CHOICES, null=False,max_length=20,default='Accepted')
    active= models.BooleanField()
    timestamp= models.DateTimeField(auto_now_add=True)

    def save(self,*args,**kwargs):

        data=self.update_desc
        if data == "Delivered":
            print("blank")
            self.order_id.mysave()
        super(Order_updates, self).save(*args, **kwargs)



