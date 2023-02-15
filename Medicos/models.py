from django.db import models

# Create your models here.

class Medicos(models.Model):
    SEXO = (
        ("M", "MASCULINO"),
        ("F", "FEMENINO"),
    )
    codigo = models.IntegerField(blank=True, null=True)
    nombres_completo = models.CharField(max_length=200)    
    especialidad = models.CharField(max_length=150, blank=True, null=True)
    imagen = models.ImageField(upload_to=('medicos/imagenes'),blank=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    centro = models.CharField(max_length=150, blank=True, null=True)
    sexo = models.CharField(max_length=10, choices=SEXO, blank=True, null=True)
    facebook  = models.CharField(max_length=150, blank=True, null=True)
    instagram = models.CharField(max_length=150, blank=True, null=True)
    is_active = models.BooleanField(default=False)
    date_joind = models.DateTimeField(auto_now_add=True)
    last_joind = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombres_completo
   
    
