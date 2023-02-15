from rest_framework import serializers
from .models import Medicos

class MedicosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicos
        fields = ('id','codigo','nombres_completo','especialidad','imagen','email','phone_number','centro','sexo','facebook','instagram','is_active','date_joind','last_joind')
        read_only_fields = ('date_joind','last_joind',)
        