from django.conf.urls import url
from app01 import views

urlpatterns = [
    url(r'^test.html$', views.test),
    url(r'^login.html$', views.login),
    url(r'^index.html$', views.index),
]