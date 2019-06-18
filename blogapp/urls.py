from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import blog_home, blog_detail,like_post, delete_comment,write_blog,search_blog,blog_edit , blog_update

app_name = 'blogapp'


urlpatterns = [
    path('', blog_home,name='blog_home'),
    path('details-/<slug:post_slug>/',blog_detail , name="second"),
    path('like_post',like_post, name='like_post'),
    path('delete/<slug:id>/',delete_comment,name='delete_comment'),
    path('write_blog',write_blog,name='write_blog'),
    path('search_blog',search_blog,name='search_blog'),
    path('blog_edit/<slug:id>/',blog_edit,name='blog_edit'),
    path('blog_update/<slug:id>/',blog_update,name='blog_update'),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
