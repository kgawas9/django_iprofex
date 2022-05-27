from dataclasses import field
from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField

from .models import Category, Course


class CategorySerializer(serializers.ModelSerializer):
    last_update = serializers.DateTimeField(read_only=True)
    class Meta:
        model = Category
        fields = [
            'id', 'title','last_update'
        ]

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = [
            'id', 'title', 'description', 'fees', 'last_updated', 'category'
        ]

    def create(self, validated_data):
        # print("inside create", validated_data)
        course = Course(**validated_data)
        course.save()
        return course

    # def update(self, instance, validated_data):
    #     instance.unit_price = validated_data.get('unit_price')
    #     instance.save()
    #     return instance