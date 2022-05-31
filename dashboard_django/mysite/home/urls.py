from django.urls import path
from . import views
from . import ka_qa
# from home.crwaling import youtube_program , naver_program

urlpatterns = [
    path('', views.home, name='home') , 
    path('temp',ka_qa.함수명, name='ka_qna')
]

# urlpatterns = [
#     path('', views.youtube_program, name='youtube_program') , 
# ]

# urlpatterns = [
#     path('', views.naver_program, name='naver_program') , 
# ]