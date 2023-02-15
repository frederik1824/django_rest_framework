from django.db import models

# Create your models here.

class Planes(models.Model):
    nombre = models.CharField(max_length=150)
    proceio = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.nombre


         