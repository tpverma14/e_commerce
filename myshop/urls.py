from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from myshop.views import home , login , category ,subcategory,product_detail
app_name = "myshop"

urlpatterns = [
    path('',home,name='home'),
    path('category/<slug:post_slug>/',category,name='category'),
    path('subcategory/<slug:post_slug>/',subcategory,name='subcategory'),
    path('product_detail/<slug:post_slug/', product_detail,name='product_details'),
    path('login',login,name="login"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
