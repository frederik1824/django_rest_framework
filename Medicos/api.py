from .models import Medicos
from rest_framework import viewsets, permissions
from .serializers import MedicosSerializer

class MedicosViewSet(viewsets.ModelViewSet):
    queryset = Medicos.objects.filter(is_active=True)
    permission_classes = [permissions.AllowAny]
    serializer_class = MedicosSerializer
    
    

