from django.db import models
import datetime
from Planes.models import Planes

# Create your models here.

class Afiliados(models.Model):
    ESTATUS_CIVIL =(
        ("SOLTERO(A)", "Soltero(a)"),
        ("CASADO(A)", "Casado(a)"),
        ("DIVORCIADO(A)", "Divorciado(a)"),
        ("VIUDO(A)", "Viudo(a)"),
    )  
    
    SEXO = (
        ("M", "MASCULINO"),
        ("F", "FEMENINO"),
    )
     
    ESTADO = (
         ("1", "ACTIVO"),
         ("2", "CANCELADO"),
         ("3", "INACTIVO POR FALTA DE PAGO"),
         ("4", "EXCLUIDO POR FALLECIMIENTO"),
         ("5", "AFILIACION AUTOMATICA"),
         ("6", "PDSS PENDIENTE DE DISPERSION"),
         ("7", "CANCELADO POR TRASPASO"),
         ("8", "EN PROCESO"),
         ("9", "EN OTRA ARS"),
         ("10", "RETIRADO, MAYORIA EDAD"),
         ("11", "OTRA POLIZA ASIGNADA"),
         ("12", "CXC VOLUNTARIOS"),
         ("14", "PENDIENTE UNIPAGO"),
         ("15", "ERROR UNIPAGO"),
         ("16", "ERROR AL VALIDAR"),
         ("17", "ERROR AL DIGITAR"),
         
     )
     
    PARENTEZCO = (
        ("TITULAR","TITULAR"),
        ("ESPOSA","ESPOSA"),
        ("HIJA","HIJA"),
        ("MADRE","MADRE"),
        ("HIJO","HIJO"),
        ("ESPOSO","ESPOSO"),
        ("HIJASTRA","HIJASTRA"),
        ("COMPAÑERO DE VIDA","COMPAÑERO DE VIDA"),
        ("PADRE","PADRE"),
        ("HIJASTRO","HIJASTRO"),
        ("SOBRINA","SOBRINA"),
        ("HIJA - TITULAR","HIJA - TITULAR"),
        ("HIJO - TITULAR","HIJO - TITULAR"),
        ("HERMANA","HERMANA"),
        ("NIETA","NIETA"),
    )

   
    Nss = models.IntegerField(unique=True, blank=True, null=True)
    Poliza = models.CharField(max_length=17, unique=True, blank=True, null=True)
    Nombre_del_Afiliado = models.CharField(max_length=200, blank=True, null=True)
    Cedula = models.CharField(max_length=200, unique=True, blank=True, null=True)
    Fecha_Nacimiento = models.DateField(max_length=14, blank=True, null=True)
    Estado_Civil = models.CharField(max_length=50, choices=ESTATUS_CIVIL, default='1', blank=True, null=True)
    Parentesco = models.CharField(max_length=25, choices=PARENTEZCO, default='1', blank=True, null=True)
    Sexo = models.CharField(max_length=25, choices=SEXO, default='1', blank=True, null=True)
    Estado = models.CharField(max_length=25, choices=ESTADO, default='1', blank=True, null=True)
    Telefono = models.CharField(max_length=17, blank=True, null=True)
    Direccion = models.CharField(max_length=400, blank=True, null=True)
    Plan = models.ForeignKey(Planes, on_delete=models.CASCADE)
    Complementario = models.BooleanField(default=False)
    
    def __str__(self):
        return self.Nombre_del_Afiliado
   






