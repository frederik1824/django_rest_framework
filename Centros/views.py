from django.shortcuts import render
from django.http import JsonResponse
from .models import Centros, Ciudad
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.

def centros(request):
    centros = Centros.objects.all().filter(estado=True)
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(centros, 15)
        centros = paginator.page(page)
    except:
        raise Http404 

    context = {
        'entity': centros,
        'paginator': paginator,
       
    }


    return render(request, 'pages/department.html', context)


'''def centrosmedicos(request):
    return render(request, 'pages/centrosmedicos.html')

def get_ciudad(_request):
    ciudad = list(Ciudad.objects.values())

    if (len(ciudad)>0):
        data={'message': "Seccess",'ciudad':ciudad}
    else:    
        data={'message': "not found"}

    return JsonResponse(data)   


def get_centros(_request, ciudad_id):
    centros = list(Centros.objects.filter(ciudad_id=ciudad_id).values())

    if (len(centros)>0):
        data={'message': "Seccess",'centros':centros}
    else:    
        data={'message': "not found"}

    return JsonResponse(data)    '''


