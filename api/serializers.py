from .models import Task, List
from rest_framework import serializers

# Serializers
class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = ['uuid', 'title', 'created_at']

        read_only_fields = ['uuid', 'created_at']

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'completed', 'updated_at']

        read_only_fields = ['id', 'updated_at']
