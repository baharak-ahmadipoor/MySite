from django.shortcuts import render

from urllib import request
from django.http import  HttpResponse, JsonResponse
from webapp1.models import contact
from webapp1.forms import contactForm, nameForm
from django.contrib import messages


def home_view(request):
    return render(request, 'index.html')

def about_view(request):
    return render(request, 'about.html')

def contact_view(request):
    if request.method == 'POST':
        form = contactForm(request.POST)
        if form.is_valid():
            form.fields['name'] = "Anonymous"
            form.save()
            messages.add_message(request, messages.SUCCESS,'your ticket submitted successfully')
        else:
            messages.add_message(request, messages.ERROR, 'Your ticket was not submitted successfully')
    form = contactForm()
    return render(request, 'contact.html',{'form':form})

def elements_view(request):
    return render(request, 'elements.html')

# test_view for normal form without model connection:
# def test_view(request):
#     if request.method == "POST":
#         form  = contactForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data["name"]
#             email = form.cleaned_data["email"]
#             subject = form.cleaned_data["subject"]
#             message = form.cleaned_data["message"]
#             print( name, email, subject, message)
#             return HttpResponse('done')
#         else:
#             return HttpResponse('error')
#     form = contactForm()
#     return render(request, 'test.html',{'form':form})


# test_view for model form with connection to model:
def test_view(request):
    if request.method == "POST":
        form  = contactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('done')
        else:
            return HttpResponse('error')
    form = contactForm()
    return render(request, 'test.html',{'form':form})