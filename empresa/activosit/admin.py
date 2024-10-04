from django.contrib import admin
from .models import Dispositivo

# Personalización del modelo Dispositivo para el admin
class DispositivoAdmin(admin.ModelAdmin):
    list_display = ('iddispositivo', 'nomenclatura', 'nrodeserie', 'jiracompra')  # Campos que se mostrarán en la lista
    search_fields = ('nomenclatura', 'nrodeserie')  # Campos por los que se podrá buscar
    list_filter = ('jiracompra',)  # Filtros laterales
    ordering = ('nomenclatura',)  # Orden por defecto

# Registra el modelo con su configuración personalizada
admin.site.register(Dispositivo, DispositivoAdmin)
