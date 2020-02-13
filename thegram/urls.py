from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^',include('gram.urls')),
    url(r'^accounts/register/$', RegistrationView.as_view(form_class=RegisterForm), name='register_to'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^logout/$', views.logout, {"next_page": 'login'}), 
    url(r'^tinymce/', include('tinymce.urls')),
]
