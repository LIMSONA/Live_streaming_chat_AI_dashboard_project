from django.urls import path
from . import views
# from . import ka_qa
# from . import cr_love


urlpatterns = [
    path('', views.home, name='home') , 
]

# path('temp',ka_qa.qa_out, name='ka_qa') ,
# path('', cr_love.youtube_love, name='cr_love') ,
# path('temp', ka_qa.qa_out, name="ka_qa") ,