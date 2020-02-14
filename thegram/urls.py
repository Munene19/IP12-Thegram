from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'',include('gram.urls')),
    url(r'accounts/',include('registration.backends.simple.urls')),

    url(r'^login/', auth_views.LoginView.as_view(template_name = 'gram/login.html'), name='login'),
    
    url(r'^logout/$', views.logout,{"next_page":'/'}),

]