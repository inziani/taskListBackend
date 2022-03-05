from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, ReadOnlyPasswordHashField
from django.contrib.auth.models import Group
from django.db import models
from .models import User, UserProfile

class CustomUserCreationForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['email']

class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']
    