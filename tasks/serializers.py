from users.serializers import serializers
from rest_framework.serializers import ModeSerializer, HyperlinkedModelSerializer
from tasks.models import Tasks

class TasksSerializer(HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Task
        fields = ('url', 'id', 'owner', 'title', 'description', 'dateCreated', 'dateChanged')