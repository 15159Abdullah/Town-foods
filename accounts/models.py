from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager


class CustomUser(AbstractUser):
    USERNAME_FIELD = 'email'
    email = models.EmailField(unique=True,default=True)
    is_admin = models.BooleanField(default=True)
    is_customer = models.BooleanField(default=False)
    REQUIRED_FIELDS = [] # removes email from REQUIRED_FIELDS
    
    def __str__(self):
        return self.username
    

    
   