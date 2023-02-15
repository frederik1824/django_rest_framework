from django.contrib import admin
from .models import Afiliados
from import_export.admin import ImportExportModelAdmin



# Register your models here.

@admin.register(Afiliados)
class userdata(ImportExportModelAdmin):
    list_display = ('Nss','Nombre_del_Afiliado', 'Cedula', 'Estado_Civil', 'Parentesco' , 'Sexo' , 'Estado' )
    list_display_link = ('Nss')
    list_filter = ('Estado','Plan',)
    ordering = ('id',)
    pass



