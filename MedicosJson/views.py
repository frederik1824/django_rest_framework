from django.shortcuts import render
import requests
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# Create your views here.


def Medicojson(request):
    
    response = requests.get('http://localhost:8000/medicos/api/medicos/')
    page = request.GET.get('page', 1)
    data = response.json()
    try:
        paginator = Paginator(data, 8)
        data = paginator.page(page)
    except:
        raise Http404 
   
    
    context = {
        'entity': data,
        'paginator': paginator,
       
    }
    
    return render(request, 'pages/medicojson.html', context)