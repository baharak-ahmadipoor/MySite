from django.urls import path
from webapp1.views import *

app_name = 'webapp1'
urlpatterns = [
    path('',home_view, name='index'),
    path('home/',home_view, name='index'),
    path('about/',about_view,name='about'),
    path('contact/',contact_view, name='contact'),
    path('elements/',elements_view, name='elements'),
    path('test/',test_view, name='test')
]

