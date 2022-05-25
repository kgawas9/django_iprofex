from django.conf import settings

from django.core.mail import send_mail
import random

from .models import User


def send_otp_via_email(email):
    subject = "Profex : Verify your email account"
    otp = random.randint(100001, 999999)
    message = f"Welcome to Profex\n\nYour otp for verification is {otp}"
    email_from = settings.EMAIL_HOST
    send_mail(subject, message, email_from, [email])
    
    user = User.objects.get(email = email)
    user.otp = str(otp)
    user.save()
