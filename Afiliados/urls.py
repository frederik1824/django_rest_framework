

from django.urls import path, include
from . import views


urlpatterns = [
    
    path('',views.afiliados, name='afiliados'),
    path('search/',views.search, name='search'),
   
]
