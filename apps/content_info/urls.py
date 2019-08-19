from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^(?P<id>[0-9]+)$', views.index),
    url(r'^(?P<id>[0-9]+)/addpost$', views.addpost),
    url(r'^(?P<id>[0-9]+)/addcomment$', views.addcomment),
    url(r'^(?P<id>[0-9]+)/deletemessage/(?P<mid>[0-9]+)$', views.deletemessage),

]