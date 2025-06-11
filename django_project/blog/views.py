from django.shortcuts import render
from django.http import HttpResponse

# Functions handle traffic from said-page of blog
# Functions take a request arguement

def home(request):
    return HttpResponse('<h1>Blog Home</h1>')

def about(request):
    return HttpResponse('<h1>Blog About</h1>')
