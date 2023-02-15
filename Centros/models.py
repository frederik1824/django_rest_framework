from django.db import models

# Create your models here.

class Ciudad(models.Model):
    nombre = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.nombre)

  
class Tipo_prestado(models.Model):
    nombre = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.nombre)



class Centros(models.Model):
    codigo = models.CharField(max_length=15, null=True, blank=True)
    nombre = models.CharField(max_length=200, null=True, blank=True)
    estado = models.BooleanField(default=True, null=True, blank=True)
    telf1 = models.CharField(max_length=20, null=True, blank=True)
    telf2 = models.CharField(max_length=20, null=True, blank=True)
    direccion = models.CharField(max_length=250, null=True, blank=True)
    ciudad = models.ForeignKey(Ciudad, null=True, blank=True, on_delete=models.CASCADE)
    tipo_prestador = models.ForeignKey(Tipo_prestado, null=True, blank=True, on_delete=models.CASCADE)
    sector = models.CharField(max_length=200, null=True, blank=True)
    numpss = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.nombre