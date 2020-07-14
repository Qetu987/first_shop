from django.contrib import admin

from course.models import Course

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name_slug', 'desc', 'name', 'meta_title', 'image_tag']
