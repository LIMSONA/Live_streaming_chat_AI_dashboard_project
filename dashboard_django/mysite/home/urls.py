from django.urls import path
from . import views
from home.crwaling import youtube_program , naver_program

urlpatterns = [
    path('', views.home, name='home') , 
]

urlpatterns = [
    path('', views.youtube_program, name='youtube_program') , 
]

urlpatterns = [
    path('', views.naver_program, name='naver_program') , 
]