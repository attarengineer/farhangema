from django.urls import path
from website.views import *

app_name = 'website'

urlpatterns = [
    path('', index_view, name='index'),
    path('home-2', home2_view, name='home-2'),
    path('contact', contact_view, name='contact'),
    path('about', about_view),
    path('http_test', http_test),
    path('json_test', json_test),
]
