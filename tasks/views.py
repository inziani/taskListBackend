from django.shortcuts import render
from rest_framework import viewsets

from .models import Tasks
from .serializers import TasksSerializer

# Create your views here.

class TasksViewSet(viewsets.ModelViewSet):
     """
    This view set automaticall provides for list, create, retrieve, update and destroy actions
    """

