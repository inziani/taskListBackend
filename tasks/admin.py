from django.contrib import admin
from .models import Tasks

# Register your models here.

taskModels = [Tasks]

admin.site.register(taskModels)
