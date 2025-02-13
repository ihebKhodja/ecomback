from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    email=models.EmailField(unique=True)
    phone= models.CharField(max_length=15, blank=True, null=True)
    address= models.TextField(blank=True, null=True)
    is_admin= models.BooleanField(default=False)
    is_client= models.BooleanField(default=True)

    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username