from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class ExtendedUser(AbstractUser):
    avatar = models.TextField(null=True, blank=True)
    phone = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    # created = models.DateTimeField(auto_now_add=True) maybe change it for default value
