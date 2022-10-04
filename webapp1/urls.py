from django.urls import path
from webapp1.views import *

app_name = 'webapp1'
urlpatterns = [
    path('',home, name='index'),
    path('home/',home, name='index'),
    path('about/',about,name='about'),
    path('contact/',contact, name='contact'),
    path('elements/',elements, name='elements')
]

