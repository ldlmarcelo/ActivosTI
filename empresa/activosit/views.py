from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Dispositivo
from django.shortcuts import get_object_or_404, render
from .models import Dispositivo, Historialubicacion  # Asegúrate de importar Historialubicacion

def lista_dispositivos(request):
    search_query = request.GET.get('search', '')
    
    if search_query:
        dispositivos = Dispositivo.objects.filter(nomenclatura__icontains=search_query)
    else:
        dispositivos = Dispositivo.objects.all()
    
    return render(request, 'lista_dispositivos.html', {'dispositivos': dispositivos, 'search_query': search_query})

def detalle_dispositivo(request, iddispositivo):
    dispositivo = get_object_or_404(Dispositivo, iddispositivo=iddispositivo)
    ubicaciones = Historialubicacion.objects.filter(dispositivo_iddispositivo=dispositivo)
    
    return render(request, 'detalle_dispositivo.html', {'dispositivo': dispositivo, 'ubicaciones': ubicaciones})

