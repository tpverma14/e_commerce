from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from myshop.views import home , log_in , category ,subcategory,product_detail ,sign_up,log_out,like
app_name = "myshop"

urlpatterns = [
    path('',home,name='home'),
    path('category/<slug:post_slug>/',category,name='category'),
    path('subcategory/<slug:post_slug>/',subcategory,name='subcategory'),
    path('product_detail/<slug:post_slug>/', product_detail,name='product_details'),
    path('login',log_in,name="login"),
    path('sign_up',sign_up,name='sign_up'),
    path('logout',log_out,name="logout"),
    path('like',like,name="like")
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
