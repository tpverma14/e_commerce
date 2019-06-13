from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from paytm.views import home,payment,response
app_name = "paytm"

urlpatterns = [
    path('',home,name='home'),
    path('payment/',payment,name='payment'),
    path('response/',response,name='response'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)