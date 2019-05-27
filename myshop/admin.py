from django.contrib import admin
from .models import Category ,Sub_Category, Product , Size_quantity , Upload_images ,Banner,Upload_data ,Category_banner ,Profile ,User
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _



# Register your models here.
def get_image_preview(obj):


    if obj.pk:
        return mark_safe('<img src="/media/%s" width="150" height="150" />' % (obj.category_image)
        # return mark_safe("""<a href="{src}" target="_blank"><img src="{src}" alt="{title}" style="max-width: 200px; max-height: 200px;" /></a>""".format(
        #     src=obj.picture.url,
        #     title=obj.product_id,
        # )
        )

    return _("(choose a picture and save and continue editing to see the preview)")

get_image_preview.short_description = _("Picture Preview")

class Category_bannerAdmin(admin.TabularInline):
    model = Category_banner
    extra = 1
    fields = ['category_image', get_image_preview]
    readonly_fields = [get_image_preview]




class CategorieAdmin(admin.ModelAdmin):

    prepopulated_fields = {'slug':('categories_name',)}
    list_display = ['categories_name','slug','updated','created']
    inlines = [Category_bannerAdmin]
admin.site.register(Category,CategorieAdmin)



class Sub_CategorieAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('product_name',)}
    list_display = ['categories','product_name','slug']


admin.site.register(Sub_Category,Sub_CategorieAdmin)


def get_picture_preview(obj):


    if obj.pk:
        return mark_safe('<img src="/media/%s" width="150" height="150" />' % (obj.image)
        # return mark_safe("""<a href="{src}" target="_blank"><img src="{src}" alt="{title}" style="max-width: 200px; max-height: 200px;" /></a>""".format(
        #     src=obj.picture.url,
        #     title=obj.product_id,
        # )
        )

    return _("(choose a picture and save and continue editing to see the preview)")

get_picture_preview.short_description = _("Picture Preview")

class Upload_imagesInline(admin.TabularInline):
    model = Upload_images
    extra = 1
    fields = ['image',get_picture_preview]
    readonly_fields = [get_picture_preview]
    raw_id_fields = ["image_id"]

class Size_quantityInline(admin.TabularInline):
    model = Size_quantity
    extra = 0
    raw_id_fields = ["product"]

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('brand_name',)}
    list_display = ['product_id','brand_name']
    inlines = [Upload_imagesInline,Size_quantityInline ]


admin.site.register(Product ,ProductAdmin)



def get_bgimage_preview(obj):


    if obj.pk:
        return mark_safe('<img src="/media/%s" width="500" height="200" />' % (obj.image)
        # return mark_safe("""<a href="{src}" target="_blank"><img src="{src}" alt="{title}" style="max-width: 200px; max-height: 200px;" /></a>""".format(
        #     src=obj.picture.url,
        #     title=obj.product_id,
        # )
        )

    return _("(choose a picture and save and continue editing to see the preview)")

get_bgimage_preview.short_description = _("Picture Preview")



class Upload_data_Admin(admin.TabularInline):
    model=Upload_data
    extra=1
    fields = ['image', get_bgimage_preview]
    readonly_fields = [get_bgimage_preview]

class Banner_Admin(admin.ModelAdmin):
    inlines = [Upload_data_Admin]
    list_display = ['name','created','updated','active']
admin.site.register(Banner , Banner_Admin)




class ProfileAdmin(admin.TabularInline):
    model=Profile
    fields = ['mobile_number']
    readonly_fields = ["mobile_number"]

class UserAdmin(admin.ModelAdmin):
    inlines = [ProfileAdmin]
    readonly_fields = ['username','email','last_name','password','first_name']
admin.site.unregister(User)
admin.site.register(User,UserAdmin)












