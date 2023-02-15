

from django.urls import path, include
from . import views


urlpatterns = [
    
    path('',views.noticias, name='noticias'),
    path('<str:id>/',views.blog_detail, name='blog_detail'),
    path('submit_review/<int:id>/',views.submit_review, name='submit_review'),
   
]
