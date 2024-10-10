from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Dispositivo

def lista_dispositivos(request):
    search_query = request.GET.get('search', '')
    
    if search_query:
        dispositivos = Dispositivo.objects.filter(nomenclatura__icontains=search_query)
    else:
        dispositivos = Dispositivo.objects.all()
    
    return render(request, 'lista_dispositivos.html', {'dispositivos': dispositivos, 'search_query': search_query})
