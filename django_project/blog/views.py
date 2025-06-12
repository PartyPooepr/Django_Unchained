from django.shortcuts import render
from django.http import HttpResponse

# Functions handle traffic from said-page of blog
# Functions take a request arguement

posts = [
    {
        'author': 'PartyPooepr',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date_posted': 'June 1, 2025'
    },
    {
        'author': 'Dummy',
        'title': 'Blog Post 2',
        'content': 'Second Post Content',
        'date_posted': 'June 3, 2025'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
