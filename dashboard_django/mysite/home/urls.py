from django.urls import path
from . import views
from . import code
# from . import cr_love


urlpatterns = [
    path('', views.home, name='home') ,
    path('tem', code.naver_host, name='naver_host') ,
    
]