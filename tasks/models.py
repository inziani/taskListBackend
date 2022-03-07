from django.db import models
from django.db.models.deletion import CASCADE, PROTECT
from django.conf import settings
from django.contrib.auth import get_user_model

# Create your models here.

class Tasks(models.Model):
    title = models.CharField(max_length=32, blank=False, default='Title') 
    description = models.CharField(max_length=132, blank=False, default='Task Details')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tasks', default=1)
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateChanged = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('dateCreated',)

    def __str__(self):
        return f'{self.title}, {self.owner}'

    def create(self, ):
        return self.save()

    def change(self, title, description ):
        self.title = title
        self.description = description
        return self.save()

