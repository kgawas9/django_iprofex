from dataclasses import field
from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField

from .models import Category, Course


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id', 'title'
        ]

class CourseSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Course
        fields = [
            'id', 'title', 'description', 'fees', 'last_updated', 'category'
        ]