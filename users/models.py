from django.contrib.auth.models import AbstractUser
from django.db import models
from users.managers import UserManager
from datetime import datetime, timedelta
from django.utils import timezone
from django.contrib.auth import get_user_model


# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=20, unique=True, default='USERNAME')
    email = models.EmailField(unique=True, null=False)
    name = models.CharField(max_length=225)
    dateOfBirth = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    REQUIRED_FIELDS = ['username','name', 'dateOfBirth']
    USERNAME_FIELD = 'email'

    objects = UserManager()

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def display_name(self):
        return f'{self.name}'
        
    def __str__(self):
        """ String representation of this User"""
        return f'{self.email}, {self.name}, {self.username}'


class UserProfile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, primary_key=True, related_name='userProfile')
    bio =  models.CharField(max_length=255, blank=True, null=True)
    hobbies = models.CharField(max_length=150, blank=True, null=True)
    create_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{ self.user.email } + " " + Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

