from django.shortcuts import render
from django.views import generic

def sociotech(request):
    return render(request, 'mysite/sociotech.html')
    

def home(request):
    return render(request, 'mysite/home.html')
