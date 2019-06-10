from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from cart.views import cart_add,cart_detail,cart_remove , coupon_avaliable , checkout ,admin_order_detail

app_name = "cart"
urlpatterns = [
    path("",cart_detail, name="cart_detail"),
    path("add/<slug:product_id>/",cart_add,name='cart_add'),
    path("remove/<slug:product_id>/",cart_remove,name='cart_remove'),
    path("coupon_avaliable",coupon_avaliable,name='coupon_avaliable'),
    path('checkout',checkout,name='checkout'),
    path('admin/order/<slug:product_id>/',admin_order_detail,name='admin_order_detail'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)