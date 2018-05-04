from django.conf.urls import url
from main import views


urlpatterns = [
    url(r'^index$', views.index),
    url(r'^genealogy$', views.home),
    url(r'^user$', views.user),
    url(r'^login$', views.login),
    url(r'^register$', views.register),
    url(r'^relogin$', views.relogin),
    url(r'^submit$', views.submit),
    url(r'^get_right$', views.get_right),
    url(r'^search$', views.search)

]