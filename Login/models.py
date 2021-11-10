from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    password_date = models.DateField(null=False, blank=True, auto_now_add=True)