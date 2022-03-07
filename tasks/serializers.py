from users.serializers import serializers
from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from tasks.models import Tasks

class TaskSerializer(HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Tasks
        fields = ('url', 'id', 'owner', 'title', 'description', 'date_created', 'date_changed')