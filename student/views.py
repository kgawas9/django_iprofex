from urllib import response
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from requests import Response

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Course, Category, Student
from .serializers import CategorySerializer, CourseSerializer, StudentSerializer

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



# Course views
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


    def post(self, request):
        try:
            serializer = CourseSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            serializer.validated_data
            serializer.save()

            return Response({
                'status': status.HTTP_201_CREATED,
                'message': 'Course successfully added',
                'data': serializer.data
            })

        except Exception as e:
            return Response({
                'status': status.HTTP_400_BAD_REQUEST,
                'message': 'Unable to create new record',
                'technical_error': str(e)
            })

    def put(self, request, id):
        try:
            course = Course.objects.get(pk=id)
            serializer = CourseSerializer(course, data=request.data)

            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({
                'status': status.HTTP_202_ACCEPTED,
                'message':'Record successfully updated',
                'data': serializer.data
            })

        except Exception as e:
            return Response({
                'status': status.HTTP_400_BAD_REQUEST,
                'message': 'Unable to update the record',
                'technical_error': str(e)
            })


# student view
class StudentView(APIView):
    def post(self, request):
        try:
            serializer = StudentSerializer(data = request.data, context = {'user_id':self.request.user.id})
            serializer.is_valid(raise_exception=True)

            serializer.validated_data
            serializer.save()

            return Response({
                    'status': status.HTTP_201_CREATED,
                    'message':'Profile successfully created',
                    'data': serializer.data
                })
        
        except Exception as e:
            return Response({
                'status': status.HTTP_400_BAD_REQUEST,
                'message':'Unable to create the profile',
                'technical_error': str(e)
            })
   
    def get(self, request):
        student = Student.objects.get(user_id=request.user.id)
        print(student)
        serializer = StudentSerializer(student)
        return Response({
                    'status': status.HTTP_200_OK,
                    'message':'Here we go',
                    'data': serializer.data
                })