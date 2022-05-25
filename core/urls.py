from django.urls import path
from .views import RegisterUserAPI, VerifyOTPAPI, ResendOTPAPI

urlpatterns = [
    path('register-user/', RegisterUserAPI.as_view(), name='register-user'),
    path('resend-otp/', ResendOTPAPI.as_view(), name='resend-otp'),
    path('verify-user/', VerifyOTPAPI.as_view(), name='verify-user'),
]