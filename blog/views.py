from django.shortcuts import render

from urllib import request
from django.http import  HttpResponse, JsonResponse

def blog_view(request):
     return render(request, 'blog/blog-home.html')

def blog_single(request):
    return render(request, 'blog/blog-single.html')

