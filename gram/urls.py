from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
    
    url(r'^', views.index, name='index'),
    url(r'^/sign-up/', views.signup)
]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)