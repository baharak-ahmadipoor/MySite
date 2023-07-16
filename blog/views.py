from django.shortcuts import render , get_object_or_404

from urllib import request
from django.http import  HttpResponse, JsonResponse
from blog.models import Post

def blog_view(request, cat_name=None):
    posts = Post.objects.filter(status = 1)
    if cat_name:
        posts = posts.filter(category__name=cat_name)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html',context)

def blog_single(request,pid):
    posts = get_object_or_404(Post, id = pid)
    context = {'posts': posts}
    return render(request, 'blog/blog-single.html',context)

def test(request):
    return render(request, 'test.html')

def blog_category(request,cat_name):
    posts = Post.objects.filter(status=1)
    posts = posts.filter(category__name=cat_name)    
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html',context)