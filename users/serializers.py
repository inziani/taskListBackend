from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from rest_framework import serializers

from .models import User, UserProfile


class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'id', 'name', 'username', 'email', 'dateOfBirth', 'is_active', 'is_staff', 'is_superuser', 'date_joined')

class UserProfileSerializer(HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(view_name = 'userprofile-detail', queryset=User.objects.all())
    class Meta:
        model = UserProfile
        fields = ('url', 'user', 'bio', 'hobbies', 'create_at', 'updated_at')