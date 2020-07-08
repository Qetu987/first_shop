from django.shortcuts import render

# Create your views here.

def index(r):
    return render(r, 'index.html', {'var': 'value'})

def about(r):
    return render(r, 'about.html', {'var': 'value'})