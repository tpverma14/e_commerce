from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import blog_home, blog_detail,like_post, delete_comment

app_name = 'blogapp'


urlpatterns = [
    path('', blog_home,name='blog_home'),
    path('details-/<slug:post_slug>/',blog_detail , name="second"),
    path('like_post',like_post, name='like_post'),
    path('delete/<slug:id>/',delete_comment,name='delete_comment'),



]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
