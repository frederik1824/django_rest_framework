from django.db import models
from django.contrib.auth.models import User
from Accounts.models import Account
from django.urls import reverse

# Create your models here.

class Blog(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Account, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to=('blog/imagenes'),blank=True)
    descripcion = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ('Blog')
        verbose_name_plural = ('Blogs')

    def get_url(self):
        return reverse('blog_detail', args=[self.id])   


    def __str__(self):
        return self.titulo


class ReviewRating(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100, blank=True)
    review = models.CharField(max_length=500, blank=True)
    rating = models.FloatField()
    ip = models.CharField(max_length=20, blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject
