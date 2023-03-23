from django.urls import path
from blog.views import *

app_name = 'blog'
urlpatterns = [
    path('index',blog_view, name='index'),
    path('single',blog_single, name='single'),
    path('post-<int:pid>',test, name='test')

]

