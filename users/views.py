from django.shortcuts import render
from rest_framework.permissions import(AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly)
from rest_framework import viewsets, status

from .models import User, UserProfile
from .serializers import UserSerializer, UserProfileSerializer, RegistrationSerializer

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """Provide list and retrieve"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class UserProfileViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

class RegistrationViewSet(viewsets.ModelViewSet):
    # Allow any user (authenticated or not) to hit this endpoint
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegistrationSerializer
    # http_method_names = ['post', 'head']

    def post(self,request):
        user = request.get('user', {})
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
