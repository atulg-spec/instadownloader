from django.db import models
from django.contrib.auth.models import AbstractUser
from backend.manager import *
from django.utils import timezone
from django.core.exceptions import ValidationError
import uuid

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=12)
    suscribed_date = models.DateTimeField(auto_now_add=True,null=True)
    expiry_date = models.DateTimeField(default=timezone.now)
    access_token = models.UUIDField(unique=True,default=uuid.uuid4,editable=False,)
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number']