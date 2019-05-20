from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from myshop.views import home , login , category
app_name = "myshop"

urlpatterns = [
    path('',home,name='home'),
    path('category-/<slug:post_slug>/',category,name='category'),
    path('login',login,name="login"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
