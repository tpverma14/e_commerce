from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe
from .models import Checkout, Oder_item , Order_updates





def order_detail(obj):
    return mark_safe('<a href="{}">View</a>'.format(reverse('cart:admin_order_detail', args=[obj.id])))
order_detail.allow_tags = True


class  Oder_itemInline(admin.TabularInline):
    model = Oder_item
    extra=0
    readonly_fields = ['product','price','order','quantity',]


class Order_updatesInlines(admin.TabularInline):
    model = Order_updates
    extra = 0
    readonly_fields = ['order_id']
    fields = ['order_id','active','update_desc']







class CheckoutAdmin(admin.ModelAdmin):

    readonly_fields = ("email", 'phone', 'address','country','first_name','last_name','postal_code','city','other_notes','coupon','discount')
    list_display = ['id', 'first_name', 'last_name', 'email',
                    'address', 'postal_code', 'city','paid',
                    'created', 'updated', order_detail]
    list_filter = [ 'paid','created', 'updated']

    inlines = [Oder_itemInline,Order_updatesInlines]





admin.site.register(Checkout, CheckoutAdmin)





