from django.urls import path
from webapp1.views import *

urlpatterns = [
    path('',home),
    path('home/',home),
    path ('about/',about),
    path('contact/',contact),
]