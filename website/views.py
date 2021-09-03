from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def http_test(request):
    return HttpResponse('<h1>salam bacheha</h1>')

def json_test(request):
    return JsonResponse({'name': 'alireza'})

def index_view(request):
    return render(request, 'index.html')

def about_view(request):
    return HttpResponse('<h1>About page</h1>')

def contact_view(request):
    return HttpResponse('<h1>Contact page</h1>')