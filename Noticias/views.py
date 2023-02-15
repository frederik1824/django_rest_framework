from django.shortcuts import render
from .models import Blog, ReviewRating
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib import messages
from .forms import ReviewForm

# Create your views here.

def noticias(request):
    blog = Blog.objects.all().order_by('-created_at')
    paginator = Paginator(blog, 6)
    page = request.GET.get('page')
    paged_blog = paginator.get_page(page)
    total_blog = blog.count()
    context = {
        'blog': paged_blog,
        'total_blog': total_blog,
    }

    return render(request, 'pages/blog.html', context)

def blog_detail(request, id):
    
    try:
        single_blog = Blog.objects.get(pk=id)
    except Exception as e:
        raise e

    reviews = ReviewRating.objects.filter(blog_id=single_blog.id, status=True)    

    context = {
        'single_blog': single_blog,
        'reviews': reviews,
        
    }    

    return render(request, 'pages/blog_detail.html',context)            


def submit_review(request, id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        try:
            reviews = ReviewRating.objects.get(user__id=request.user.id, blog__id=id)
            form = ReviewForm(request.POST, instance=reviews)
            form.save()
            messages.success(request, 'Muchas Gracias!, tu comentario ha sido actualizado')
            return redirect(url)
        except ReviewRating.DoesNotExist:
            form = ReviewForm(request.POST)
            if form.is_valid():
                data = ReviewRating()
                data.subject = form.cleaned_data['subject']
                data.rating = form.cleaned_data['rating']
                data.review = form.cleaned_data['review']
                data.ip = request.META.get('REMOTE_ADDR')
                data.id = id
                data.user_id = request.user.id
                data.save()
                messages.success(request, 'Muchas gracias!, tu comentario fue enviado con exito')
                return redirect(url)
