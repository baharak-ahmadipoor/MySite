from django.shortcuts import render

from urllib import request
from django.http import  HttpResponse, JsonResponse

def home(request):
    return HttpResponse("<h1>This is Home page</h1>")

def about(request):
    return HttpResponse("<h1>This is About page</h1>")

def contact(request):
    return HttpResponse("<h1>This is Contact page</h1>")