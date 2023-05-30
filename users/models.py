from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime


# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    dob = models.DateField(null=True)
    city = models.CharField(max_length=255, null=True)
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.username
