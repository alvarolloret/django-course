from django.conf.urls import url, include
from users_app import views

urlpatterns = [
    url(r'^$', views.viewusers, name='viewusers'),
]
