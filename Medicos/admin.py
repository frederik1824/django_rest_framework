from django.contrib import admin
from .models import Medicos
from import_export.admin import ImportExportModelAdmin

# Register your models here.

@admin.register(Medicos)
class MedicosAdmin(ImportExportModelAdmin):
    list_display = ('nombres_completo','especialidad')
    list_filter = ('especialidad', 'centro', 'is_active')

