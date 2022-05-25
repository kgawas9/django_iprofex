from django.http import JsonResponse
from django.shortcuts import render
from requests import Response

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Course
from .serializers import CourseSerializer

# Create your views here.

class CourseSerializerView(APIView):
    def get(self, request):
        queryset = Course.objects.all()
        try:
            serializer = CourseSerializer(queryset, many=True)
            # return the response
            return Response({
                    'status': status.HTTP_200_OK,
                    'message': 'Successfully fetched the data from database',
                    'data': serializer.data
                })
        except Exception as e:
            return Response({
                    'message':'Unable to fetch data from system',
                    'technical_error': str(e)
                })

