from django.contrib import admin
from django.conf.urls.static import static
from django.conf.urls import url
from . import views as home_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    url(r'^$',home_view.index,name='index'),
    url(r'^home/$',home_view.home,name='home'),
    url(r'^image/$', home_view.image_upload,name='upload'),
    url(r'^profile/$', home_view.profile_info,name='profile'),
    url(r'^edit/$',home_view.profile_edit,name='edit'),
    url(r'^new_comment/(\d+)/$' ,home_view.add_comment,name='newComment'),
    url(r'^comment/(\d+)/$' ,home_view.comments,name='comments'),
    url(r'^likes/(\d+)/$' , home_view.like_images, name='likes'),
    url(r'^user/$',home_view.search_user,name='search_user')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

    