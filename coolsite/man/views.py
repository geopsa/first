from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('Hello, this is animal world')

def sait(request):
    return render(request, template_name='base.html')
