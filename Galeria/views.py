from django.shortcuts import render
from .models import Galeria

# Create your views here.

from django.shortcuts import render

# Create your views here.


def galeria(request):
    galeria = Galeria.objects.all().order_by('date_joind')
    context = {
        'galeria': galeria,
    }
    return render(request, 'pages/gallery.html', context)