from django.contrib import admin
from django.urls import reverse

from .models import Checkout, Oder_item




def order_detail(obj):
    return '<a href="{}">View</a>'.format(reverse('cart:admin_order_detail', args=[obj.id]))
order_detail.allow_tags = True



class  Oder_itemInline(admin.TabularInline):
    model = Oder_item
    readonly_fields = ['product','price','order','quantity']




class CheckoutAdmin(admin.ModelAdmin):
    readonly_fields = ("email", 'phone', 'address')
    list_display = ['id', 'first_name', 'last_name', 'email',
                    'address', 'postal_code', 'city', 'paid',
                    'created', 'updated', order_detail ]
    list_filter = ['paid', 'created', 'updated']
    inlines = [Oder_itemInline]


admin.site.register(Checkout, CheckoutAdmin)









