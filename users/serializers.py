from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from rest_framework import serializers

from .models import User, UserProfile


class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'id', 'name', 'username', 'email', 'dateOfBirth', 'is_active', 'is_staff', 'is_superuser', 'date_joined')

class UserProfileSerializer(HyperlinkedModelSerializer):
    #Displays user Profiles
    user = serializers.HyperlinkedRelatedField(view_name = 'userprofile-detail', queryset=User.objects.all())
    class Meta:
        model = UserProfile
        fields = ('url', 'user', 'bio', 'hobbies', 'create_at', 'updated_at')

class RegistrationSerializer(HyperlinkedModelSerializer):
    """ Serializer registration requests and creates new user"""
    password = serializers.CharField(
        max_length = 128,
        min_length = 12,
        write_only = True
    )

    # The client should not be able to send a token along with a registration request. Make the request readonly to handle it.
    token = serializers.CharField(max_length=255, read_only = True)

    class Meta:
        model = User
        # List all the fields that could possible be included in a request or response including fields specified explicitly above
        fields = ['id','username','email', 'name','dateOfBirth', 'token', 'password']

    def create(self, validated_data):
        # Use the create_user method to create new user
        return User.objects.create_user(**validated_data)
