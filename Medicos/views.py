from django.shortcuts import render
from .models import Medicos
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# Create your views here.


def medicos(request):


    medicos = Medicos.objects.all().filter(is_active=True)
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(medicos, 8)
        medicos = paginator.page(page)
    except:
        raise Http404 

    context = {
        'entity': medicos,
        'paginator': paginator,
       
    }


    return render(request, 'pages/doctors.html', context)