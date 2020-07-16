from django.shortcuts import render

from course.models import Course

# Create your views here.

def index(r):
    courses = Course.objects.all()
    return render(r, 'index.html', {'courses': courses})

def about(r):
    return render(r, 'about.html', {'var': 'value'})