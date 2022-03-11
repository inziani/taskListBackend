from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, ReadOnlyPasswordHashField
from django.contrib.auth.models import Group
from django.db import models
from .models import User, UserProfile

class RegistrationForm(forms.ModelForm):
  password = forms.CharField(label='Password', widget=forms.PasswordInput)

  class Meta:
    model = User
    fields = ('email','name', 'dateOfBirth')

  def save(self, commit=True):
    # Save the password in a hashed format
    user = super().save(commit=False)
    user.set_password(self.cleaned_data['password'])
    if commit:
      user.save()
    return user

class CustomUserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']

class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']
    