

from django.urls import path, include
from . import views


urlpatterns = [
    
    path('',views.home, name='home'),
    path('nosotros/',views.about, name='about'),
    path('contact/',views.contact, name='contact'),
]
