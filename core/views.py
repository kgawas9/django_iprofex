from os import stat
from urllib import response
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .models import User

from .serializers import UserCreateSerializer, AccountVerifySerializer, ResendOTPSerializer
from .emails import send_otp_via_email
# Create your views here.

class RegisterUserAPI(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = UserCreateSerializer(data = data)
            if serializer.is_valid():
                serializer.save()
                send_otp_via_email(serializer.data['email'])

                return Response({
                    'status': status.HTTP_200_OK,
                    'message': 'Registration successful, check email to verify your account',
                    'data': serializer.data
                })
            
            return Response({
                'status':status.HTTP_400_BAD_REQUEST,
                'message': "Bad request! Something went wrong",
                'data': serializer.errors
            })

        except Exception as e:
            print(e)


class VerifyOTPAPI(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = AccountVerifySerializer(data = data)

            if serializer.is_valid():
                email = serializer.data['email']
                otp = serializer.data['otp']

                usr = User.objects.filter(email = email)

                if not usr.exists():
                    return Response({
                        'status': status.HTTP_204_NO_CONTENT,
                        'message': 'User does not found in database',
                        'data': serializer.errors
                    })

                if not usr[0].otp == otp:
                    return Response({
                        'status': status.HTTP_400_BAD_REQUEST,
                        'message': 'Invalid otp - please enter the correct otp',
                        'data': serializer.errors
                    }, status= status.HTTP_400_BAD_REQUEST)


                usr = usr.first()
                usr.is_verified = True
                usr.otp = "Done"
                usr.save()

                return Response({
                    'status': status.HTTP_202_ACCEPTED,
                    'message': 'OTP Verified'
                }, status= status.HTTP_202_ACCEPTED)

        
        except Exception as e:
            print(e)

class ResendOTPAPI(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = ResendOTPSerializer(data = data)

            if serializer.is_valid():
                email = serializer.data['email']
                send_otp_via_email(email)

                return Response({
                    'status': status.HTTP_200_OK,
                    'message': 'OTP successfully sent to an email: ' + str(email)
                })
            
            return Response({
                'status': status.HTTP_400_BAD_REQUEST,
                'message': 'Something went wrong, please provide the correct details..'
            })
        
        except:
            return Response({
                'status': status.HTTP_400_BAD_REQUEST,
                'message': "Something went wrong, please prvide the correct details.."
            })
