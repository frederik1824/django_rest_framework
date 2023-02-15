from django.shortcuts import render
from Noticias.models import Blog
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.

def home(request):

    blog = Blog.objects.all().order_by('-created_at')
    paginator = Paginator(blog, 3)
    page = request.GET.get('page')
    paged_blog = paginator.get_page(page)
    total_blog = blog.count()
    context = {
        'blog': paged_blog,
        'total_blog': total_blog,
    }
    
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    return render(request, 'pages/contact.html')
