from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^sucessfullogin/(?P<id>[0-9]+)$', views.sucessfullogin),
    url(r'^destroy$', views.logout)

    # url(r'^admin/', admin.site.urls),
]

