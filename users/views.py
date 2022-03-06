from django.shortcuts import render
from rest_framework import viewsets, status

from .models import User, UserProfile
from .serializers import UserSerializer, UserProfileSerializer

# Create your views here.

"""
    API endpoint that allows users to be viewed or edited.
    """

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """Provide list and retrieve"""
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserProfileViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
