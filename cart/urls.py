from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from cart.views import cart

app_name = "cart"
urlpatterns = [
    path("",cart,name="cart")




]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)