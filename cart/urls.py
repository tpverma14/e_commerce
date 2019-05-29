from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from cart.views import cart_add,cart_detail,cart_remove

app_name = "cart"
urlpatterns = [
    path("",cart_detail, name="cart_detail"),
    path("<slug:product_id>",cart_add,name='cart_add'),
    path("<slug:product_id>",cart_remove,name='cart_remove'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)