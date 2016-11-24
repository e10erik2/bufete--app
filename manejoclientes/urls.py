from django.conf.urls import include, url
from . import views

urlpatterns = [
        url(r'^$', views.client_list),
        url(r'^client/(?P<pk>[0-9]+)/$', views.client_detail),
]