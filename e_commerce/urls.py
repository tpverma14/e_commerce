"""e_commerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from myshop import urls as myshop_url
from django.conf import settings
from django.conf.urls.static import static
from cart import urls as cart_url
from coupon import urls as coupon_url
from paytm import urls as paytm_urls
from blogapp import urls as blog_urls

urlpatterns = [

    path('admin/', admin.site.urls),
    path('',include(myshop_url)),
    path('cart/',include(cart_url)),
    path('coupon/',include(coupon_url)),
    path('paytm/',include(paytm_urls)),
    path('blogapp/',include(blog_urls)),




]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
