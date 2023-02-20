

from django.urls import path, include
from . import views


urlpatterns = [
    
    path('',views.galeria, name='galeria'),
    path('json/',views.hello_user, name='galeriajson'),
   
]
