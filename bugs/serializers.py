from rest_framework import serializers
from.models import Bug

class BugSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bug
        fields = ['id', 'title', 'description', 'status', 'created_at'] 
        read_only_fields = ['id', 'created_at']