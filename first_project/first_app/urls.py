from django.conf.urls import url, include
from first_app import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^$', views.help, name='help'),
    url(r'^$', views.photo, name='photo'),
    url(r'^$', views.photo, name='mtv'),

]
