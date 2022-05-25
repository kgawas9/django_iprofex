from django.contrib import admin

from .models import Category, Course

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'title', 'description'
    ]

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'title', 'description', 'fees', 'last_updated', 'category'
    ]
