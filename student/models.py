from django.db import models
from django.contrib import admin

from django.core.validators import MinValueValidator
from django.conf import settings

from uuid import uuid4

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    fees = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    last_updated = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, related_name='course_category')
    
    def __str__(self):
        return self.title
    

class Student(models.Model):
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'

    STUD_MEMBERSHIP = [
        (MEMBERSHIP_BRONZE, 'Bronze'),
        (MEMBERSHIP_SILVER, 'Silver'),
        (MEMBERSHIP_GOLD, 'Gold'),
    ]
    
    mobile_no = models.CharField(max_length=15, unique=True)
    birth_date = models.DateField()
    membership = models.CharField(max_length=1, choices=STUD_MEMBERSHIP, default=MEMBERSHIP_BRONZE)

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.first_name}'

    @admin.display(ordering='user__first_name')
    def first_name(self):
        return self.user.first_name

    @admin.display(ordering='user__last_name')
    def last_name(self):
        return self.user.last_name


class CourseEnrollment(models.Model):
    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_COMPLETE = 'C'
    PAYMENT_STATUS_FAILED = 'F'
    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_STATUS_PENDING, 'Pending'),
        (PAYMENT_STATUS_COMPLETE, 'Complete'),
        (PAYMENT_STATUS_FAILED, 'Failed')
    ]
    
    enrolled_at = models.DateTimeField(auto_now=True)
    payment_status = models.CharField(
        max_length=1, choices=PAYMENT_STATUS_CHOICES, default=PAYMENT_STATUS_PENDING)
    student = models.ForeignKey(Student, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.student}'


class CourseItem(models.Model):
    enrollment = models.ForeignKey(CourseEnrollment, on_delete=models.PROTECT, related_name='items')
    course = models.ForeignKey(
        Course, on_delete=models.PROTECT, related_name='courseitems')
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)


class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    postalcode = models.CharField(max_length=6)
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE)


class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE, related_name='items')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1)]
    )

    class Meta:
        unique_together = [['cart', 'course']]

    def __str__(self):
        return str(self.cart.id)
