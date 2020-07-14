from django.contrib import admin

from course.models import Course, Lesson, Topic


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name_slug', 'desc', 'name', 'meta_title', 'image_tag']


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title', 'number']


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ['title', 'filename', 'lesson']