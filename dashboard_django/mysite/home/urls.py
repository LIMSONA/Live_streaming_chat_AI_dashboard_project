from django.urls import path
from . import views
# from . import code
# from ...fx_django import cr_host
from . import cr_host

urlpatterns = [
    path('', views.home, name='home') ,
    path('tem', cr_host.naver_host, name='naver_host') ,
]