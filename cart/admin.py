from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe
from .models import Checkout, Oder_item
from django.utils.translation import ugettext_lazy as _




def order_detail(obj):
    return mark_safe('<a href="{}">View</a>'.format(reverse('cart:admin_order_detail', args=[obj.id])))
order_detail.allow_tags = True




# get_image_preview.short_description = _("Picture Preview")

class  Oder_itemInline(admin.TabularInline):
    model = Oder_item
    readonly_fields = ['product','price','order','quantity',]




class CheckoutAdmin(admin.ModelAdmin):
    readonly_fields = ("email", 'phone', 'address','country','first_name','last_name','postal_code','city','other_notes','coupon','discount')
    list_display = ['id', 'first_name', 'last_name', 'email',
                    'address', 'postal_code', 'city', 'paid',
                    'created', 'updated', order_detail ]
    list_filter = ['paid', 'created', 'updated']
    inlines = [Oder_itemInline]


admin.site.register(Checkout, CheckoutAdmin)









