from django.db import models
from django.urls import reverse

# Create your models here.

class Servicios(models.Model):
    nombre = models.CharField(max_length=150)
    imagen = models.ImageField(upload_to=('blog/imagenes'),blank=True)
    descripcion = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ('servicio')
        verbose_name_plural = ('servicios')

    def get_url(self):
        return reverse('servicio_detail', args=[self.id])   

    def __str__(self):
        return self.nombre
