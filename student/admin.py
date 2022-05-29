from django.contrib import admin

from .models import Cart, CartItem, Category, Course, CourseEnrollment, CourseItem, Student

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

@admin.register(Student)
class StudAdmin(admin.ModelAdmin):
    list_display = [
        'first_name', 'last_name', 'birth_date', 'membership'
    ]


@admin.register(CourseEnrollment)
class CourseEnrollmentAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'payment_status', 'enrolled_at'
    ]

@admin.register(CourseItem)
class CourseItemAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'quantity', 'unit_price'
    ]


admin.site.register(Cart)    

admin.site.register(CartItem)