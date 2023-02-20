from django.shortcuts import render
from .models import Galeria
from .services import get_username

# Create your views here.

from django.shortcuts import render

# Create your views here.


def galeria(request):
    galeria = Galeria.objects.all().order_by('date_joind')
    context = {
        'galeria': galeria,
    }
    return render(request, 'pages/gallery.html', context)

from .services import get_username


def hello_user(requests):
    context = {
        'name': get_username()
    }
    
    print(context)
    return render(requests, 'pages/gallery.html', context)
#Si así lo deseamos poder enviar parametros a nuestra petición.

def hello_user(requests):
    params = { 'order': 'desc' }

    context = {
        'name': get_username(params)
    }
    return render(requests, 'hello_user.html', context)