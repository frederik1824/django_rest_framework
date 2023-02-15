from django.db import models

# Create your models here.


class Galeria(models.Model):
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField(null=True, blank=True)
    imagen = models.ImageField(upload_to=('galeria/imagen'))
    date_joind = models.DateTimeField(auto_now_add=True)
    last_joind = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

