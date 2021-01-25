from django.conf.urls import url
from app01 import views

urlpatterns = [
    url(r'login.html/', views.Login.as_view, name='login'),
    url(r'test.html', views.test, name='test'),
    url(r'index.html', views.index, name='index'),
    url(r'customer.html', views.customer, name='customer'),
    url(r'test_xss.html', views.test_xss),
    url(r'comment.html', views.comment),
    url(r'csrf1.html', views.csrf1),
]
