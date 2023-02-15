from django.contrib import admin
from .models import Planes

# Register your models here.

class PlanesAdmin(admin.ModelAdmin):
    list_display = ['id','nombre' ]
   

admin.site.register(Planes, PlanesAdmin)