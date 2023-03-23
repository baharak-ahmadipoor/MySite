from django.urls import path
from django.conf import settings
from .views import second

urlpatterns = [
    path('secondapp/',second)
  
]