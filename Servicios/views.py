from django.shortcuts import render
from .models import Servicios

# Create your views here.


def servicios(request):
    servicios = Servicios.objects.all()
    context = {
        'servicios' : servicios
    }

    
    return render(request, 'pages/services.html', context)


def servicio_detail(request, id):
    
    try:
        single_service = Servicios.objects.get(pk=id)
    except Exception as e:
        raise e

    context = {
        'single_service': single_service,
        
    }    

    return render(request, 'pages/servicio_detail.html',context)     

servicio_detail    