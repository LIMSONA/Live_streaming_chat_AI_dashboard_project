from django.urls import path
from . import views
from . import livecommerce

urlpatterns = [
    path('', views.home, name='home') ,
    path('tem', livecommerce.naver_host, name='naver_host') ,
]