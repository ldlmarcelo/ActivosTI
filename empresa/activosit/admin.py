from django.contrib import admin
from .models import Dispositivo, Historialubicacion, UbicEspecifica, Ubicacion


@admin.register(Dispositivo)
class DispositivoAdmin(admin.ModelAdmin):
    list_display = ('nomenclatura', 'nrodeserie')  # Campos a mostrar en la lista
    search_fields = ('nomenclatura', 'nrodeserie')  # Habilita el campo de búsqueda
    list_filter = ('nomenclatura',)  # Filtros por número de serie


@admin.register(Historialubicacion)
class HistorialubicacionAdmin(admin.ModelAdmin):
    list_display = ('dispositivo_iddispositivo', 'ubic_especifica_idubic_especifica', 'fecha')  # Campos a mostrar en la lista
    search_fields = ('dispositivo_iddispositivo__nomenclatura', 'ubic_especifica_idubic_especifica__ubic_especifica')  # Búsqueda por nombre del dispositivo y ubicación específica
    list_filter = ('fecha', 'ubic_especifica_idubic_especifica')  # Filtros por fecha y ubicación específica


@admin.register(UbicEspecifica)
class UbicEspecificaAdmin(admin.ModelAdmin):
    list_display = ('ubic_especifica', 'ubicacion_idubicacion')  # Campos a mostrar en la lista
    search_fields = ('ubic_especifica', 'ubicacion_idubicacion__ubicacion')  # Búsqueda por nombres de ubicaciones
    list_filter = ('ubicacion_idubicacion',)  # Filtros por ubicación general


@admin.register(Ubicacion)
class UbicacionAdmin(admin.ModelAdmin):
    list_display = ('ubicacion',)  # Mostrar solo el campo 'ubicacion'
    search_fields = ('ubicacion',)  # Búsqueda por nombre de la ubicación
