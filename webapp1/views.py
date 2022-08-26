from django.shortcuts import render

from urllib import request
from django.http import  HttpResponse, JsonResponse


def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def elements(request):
    return render(request, 'elements.html')