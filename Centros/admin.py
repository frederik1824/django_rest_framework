from django.contrib import admin
from .models import Centros, Ciudad, Tipo_prestado
from import_export.admin import ImportExportModelAdmin


# Register your models here.

@admin.register(Ciudad)
class userdata(ImportExportModelAdmin):
    list_display = ('nombre', )
    list_display_link = ('nombre')
    ordering = ('created_at',)
    pass

@admin.register(Tipo_prestado)
class userdate(ImportExportModelAdmin):
    list_display = ('id','nombre', )
    list_display_link = ('nombre')
    ordering = ('created_at',)
    pass

@admin.register(Centros)
class userdat(ImportExportModelAdmin):
    list_display = ('codigo', 'nombre', 'estado', 'telf1', 'telf2', 'direccion', 'tipo_prestador','ciudad', 'numpss', )
    list_display_link = ('codigo', 'numpss')
    readonly_fields = ('estado', )
    ordering = ('codigo',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    pass

