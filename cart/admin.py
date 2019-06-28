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
    fields = ['order_id','active','update_desc']


    def get_readonly_fields(self, request, obj=None):
        if obj:
            print(obj.order_id.update_desc )
            if obj.order_id.update_desc == "Delivered":
                return self.readonly_fields + ('update_desc',)
        return self.readonly_fields

    # def get_exclude(self, request, obj=None):
    #     if obj:
    #         print(obj.order_id.update_desc)
    #         self.fields.remove('title')
    #     return self.exclude






class CheckoutAdmin(admin.ModelAdmin):

    readonly_fields = ('checkout_id',"email", 'phone', 'address','country','city','first_name','last_name','postal_code','other_notes','coupon','discount','paid')
    # fields = ['checkout_id',"email", 'phone', 'address',('country','city'),('first_name','last_name'),'postal_code','other_notes','coupon','discount','paid']
    list_display = ['id', 'first_name', 'last_name', 'email',
                    'address', 'postal_code', 'city','paid',
                    'created', 'updated', order_detail]
    list_filter = [ 'paid','created', 'updated']
    fieldsets = [
        ['Billing Information', {
            'fields': ['checkout_id',"email", 'phone', 'address',('country','city'),('first_name','last_name'),'postal_code','other_notes']
        }],
        ['Paid Status', {
            # 'classes': ['collapse'],
            'fields': ['paid'],
        }],
        ['Any Coupon Applied', {
            'classes': ['collapse'],
            'fields': ['coupon', 'discount'],
        }],
    ]

    inlines = [Oder_itemInline,Order_updatesInlines]





admin.site.register(Checkout, CheckoutAdmin)





