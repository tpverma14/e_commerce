from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from coupon.views import coupon_apply
app_name= 'coupon'
urlpatterns = [
    path("apply",coupon_apply,name='coupon_apply')



]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)