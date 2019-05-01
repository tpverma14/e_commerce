
from django.urls import path
from myshop.views import home , login
app_name = "myshop"

urlpatterns = [
    path('',home,name='home'),
    path('login',login,name="login")
]
