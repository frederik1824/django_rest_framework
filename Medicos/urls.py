from rest_framework import routers
from .api import MedicosViewSet
from django.urls import path, include
from . import views


router = routers.DefaultRouter()

router.register('api/medicos', MedicosViewSet, 'medicos')


urlpatterns = router.urls
