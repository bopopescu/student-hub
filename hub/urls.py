from django.conf.urls import patterns, url
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView
from hub import views

urlpatterns = patterns('',
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', views.login ,name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^home/$', views.home, name='home'),
    url(r'^index/$', views.index, name='index'),
    url(r'^results/$', views.results, name='results'),
    url(r'^edit_info/$', views.edit_info, name='edit_info'),


)