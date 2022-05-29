from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField
from django.db import transaction

from .models import Cart, Category, Course, Student


class CategorySerializer(serializers.ModelSerializer):
    last_update = serializers.DateTimeField(read_only=True)
    class Meta:
        model = Category
        fields = [
            'id', 'title','last_update'
        ]

class CourseSerializer(serializers.ModelSerializer):
    last_updated = serializers.DateTimeField(read_only=True)
    class Meta:
        model = Course
        fields = [
            'id', 'title', 'description', 'fees', 'last_updated', 'category'
        ]
        depth = 1

    def create(self, validated_data):
        # print("inside create", validated_data)
        course = Course(**validated_data)
        course.save()
        return course


    # update fees, title, category and description
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title')
        instance.description = validated_data.get('description')
        instance.fees = validated_data.get('fees')
        instance.category = validated_data.get('category')

        instance.save()
        return instance

# student serializer
class StudentSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Student
        fields = [
            'mobile_no', 'birth_date', 'membership', 'user_id'
        ]
        depth = 1

    def create(self, validated_data):
        student = Student(**validated_data, user_id=self.context['user_id'])
        student.save()
        return student


# cart serializer
class CartSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = Cart
        fields = [
            'id'
        ]

    def create(self, validated_data):
        cart = Cart(**validated_data)
        cart.save()
        return cart

