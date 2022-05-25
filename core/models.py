from django.contrib.auth.models import AbstractUser
from django.db import models

from .manager import UserManager

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True)
    is_verified = models.BooleanField(default=False)

    otp = models.CharField(max_length=6, null=True, blank=True)

    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELD = ['username']

    objects = UserManager()

    def name(self):
        return self.first_name

    def str(self):
        return self.email

