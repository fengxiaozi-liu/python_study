from django.conf.urls import url
from app01.views import account, love

urlpatterns = [
    url(r'^login.html$', account.login),
    url(r'^logout.html$', account.logout),
    url(r'^index.html$', love.index),
    url(r'^others.html$', love.others),

]
