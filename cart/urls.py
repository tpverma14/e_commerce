from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from cart.views import cart_add,cart_detail,cart_remove , coupon_avaliable , checkout \
    ,admin_order_detail,  empty_cart ,checkout_page , generate_Pdf ,  tracker

app_name = "cart"

urlpatterns = [
    path("",cart_detail, name="cart_detail"),
    path("add/<slug:product_id>/",cart_add,name='cart_add'),
    path("remove/<slug:product_id>/",cart_remove,name='cart_remove'),
    path("coupon_avaliable",coupon_avaliable,name='coupon_avaliable'),
    path('checkout',checkout,name='checkout'),
    path('admin/order/<slug:product_id>/',admin_order_detail,name='admin_order_detail'),
    path("empty_cart",empty_cart,name='empty_cart'),
    path('checkout_page',checkout_page,name='checkout_page'),
    path('generate_Pdf/',generate_Pdf,name='generate_Pdf'),
    path("tracker/<slug:id>/",tracker,name='tracker'),


]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)