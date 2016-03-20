from django.conf.urls import url
from . import views

urlpatterns = [
    
    url(r'login/$', views.user_login, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^topup/$', views.topup, name='topup'),
    url(r'^home/$', views.home, name='home'),
    url(r'^', views.home, name='home'),
    url(r'^log/$', views.transaction_log, name='transaction_log'),
]