from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    name = request.GET.get('name', '匿名')
    return HttpResponse(f'Hello {name}.')
