from django.shortcuts import render
from .models import Planes

# Create your views here.


def planes(request):
    planes = Planes.objects.all()

    context = {
        'planes': planes,
    }
    return render(request, 'pages/planes.html', context)