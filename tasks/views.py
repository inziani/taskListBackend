from django.shortcuts import render
from rest_framework.permissions import(AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly)
from rest_framework import viewsets

from .models import Tasks
from .serializers import TaskSerializer

# Create your views here.

class TasksViewSet(viewsets.ModelViewSet):

    """
    This view set automaticall provides for list, create, retrieve, update and destroy actions
    """
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [ IsAuthenticatedOrReadOnly, IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

