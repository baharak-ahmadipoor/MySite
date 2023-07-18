from django.shortcuts import render

from urllib import request
from django.http import  HttpResponse, JsonResponse
from webapp1.models import contact
from webapp1.forms import nameForm


def home_view(request):
    return render(request, 'index.html')

def about_view(request):
    return render(request, 'about.html')

def contact_view(request):
    return render(request, 'contact.html')

def elements_view(request):
    return render(request, 'elements.html')

def test_view(request):
    if request.method == "POST":
        form  = nameForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            subject = form.cleaned_data["subject"]
            message = form.cleaned_data["message"]
            print( name, email, subject, message)
            return HttpResponse('done')
        else:
            return HttpResponse('error')
    form = nameForm()
    return render(request, 'test.html',{'form':form})