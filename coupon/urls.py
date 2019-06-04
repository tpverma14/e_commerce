from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from coupon.views import coupon_apply , coupon_remove
app_name= 'coupon'
urlpatterns = [
    path("apply",coupon_apply,name='apply'),
    path("remove",coupon_remove,name='remove')


]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)