from django.contrib import admin

# Register your models here.
from index.models import Page

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ['title', 'content']
    search_fields = ['title']
