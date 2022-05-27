from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from requests import Response

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Course, Category
from .serializers import CategorySerializer, CourseSerializer

# Create your views here.

class CategoryView(APIView):
    def get(self, request, id=None):
        try:
            if id is not None:
                category = Category.objects.get(pk=id)
                serializer = CategorySerializer(category)
            else:
                categories = Category.objects.all()
                serializer = CategorySerializer(categories, many=True)

            return Response({
                'status': status.HTTP_200_OK,
                'message': 'successfully fetched all categories',
                'data': serializer.data
            })
        except Exception as e:
            return Response({
                'status': status.HTTP_400_BAD_REQUEST,
                'message':'Unable to fetch data from system',
                'technical_error': str(e)
            })

    def post(self, request):
        try:
            serializer = CategorySerializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            serializer.validated_data
            serializer.save()
            
            return Response({
                    'status': status.HTTP_201_CREATED,
                    'message': 'successfully fetched all categories',
                    'data': serializer.data
                })
        except Exception as e:
            return Response({
                'status': status.HTTP_400_BAD_REQUEST,
                'message':'Unable to create new record',
                'technical_error': str(e)
            })




class CourseView(APIView):
    def get(self, request, id=None):
        try:
            if id is not None:
                query = Course.objects.select_related('category').get(pk=id)
                serializer = CourseSerializer(query)
            else:
                queryset = Course.objects.select_related('category').all()    
                serializer = CourseSerializer(queryset, many=True)
                # return the response
            return Response({
                    'status': status.HTTP_200_OK,
                    'message': 'Successfully fetched the data from database',
                    'data': serializer.data
                })
        except Exception as e:
            return Response({
                    'status': status.HTTP_400_BAD_REQUEST,
                    'message':'Unable to fetch data from system',
                    'technical_error': str(e)
                })

