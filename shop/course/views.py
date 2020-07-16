from django.shortcuts import render
from .models import Course, Lesson, Topic

def course_detail(request,slug):
    course = Course.objects.get(name_slug=slug)
    lessons = Lesson.objects.filter(course=course)
    return render(request,'course_detail.html',{'course': course, 'lessons': lessons})



def lesson_detail(request,slug):
    lesson = Lesson.objects.get(name_slug=slug)
    topics = Topic.objects.filter(lesson=lesson)
    print(topics)
    return render(request,'lesson_detail.html',{'lesson': lesson, 'topics': topics})
