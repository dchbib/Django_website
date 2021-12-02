from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from accounts import views as accounts_views


urlpatterns = [
    url(r'^$', accounts_views.Welcome.as_view(), name='home'),
    url(r'^signup/$', accounts_views.signup, name='signup'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'), 

    url(r'^settings/account/$', accounts_views.UserUpdateView.as_view(), name='my_account'),
    
    url(r'^contact/', accounts_views.contact, name='contact'),
    
    url(r'^cv/', accounts_views.cv, name='curriculumvitae'), 
    
    url(r'^admin/', admin.site.urls),
]

