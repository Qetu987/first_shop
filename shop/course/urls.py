from django.urls import path, include
from .views import course_detail, lesson_detail

urlpatterns = [ 
    path('<slug:slug>',course_detail, name="course_detail"),
    path('lesson/<slug:slug>',lesson_detail, name="lesson_detail"),
]

