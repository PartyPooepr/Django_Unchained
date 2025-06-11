# similar to urls.py from django_project
from django.urls import path
from . import views

# urlpatterns points to the functions in views.py
urlpatterns = [
    path('', views.home, name = 'blog-home'),
    # leave path empty for HOME
    path('about/', views.about, name = 'blog-about')
]
