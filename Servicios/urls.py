

from django.urls import path, include
from . import views


urlpatterns = [
    
    path('',views.servicios, name='servicios'),
    path('<str:id>/',views.servicio_detail, name='servicio_detail'), 
]
