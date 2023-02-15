from django.shortcuts import render
from .models import Afiliados

# Create your views here.

def afiliados(request):
       
    afiliado= Afiliados.objects.all()
    context = {
        'afiliado': afiliado,
    }
    return render(request, 'pages/afiliados.html', context)


def search(request):
    
    buscarafiliado = request.GET["buscarafiliado"]
    afiliado_consulta = Afiliados.objects.filter(Cedula__icontains=buscarafiliado)
    context = {
        'buscarafiliado': buscarafiliado,
        'afiliado_consulta': afiliado_consulta,
    }
    return render(request, 'pages/search.html', context)

    
