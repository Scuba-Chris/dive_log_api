from rest_framework import serializers
from .models import DiveLog

class DiveLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiveLog
        fields = [
            'id', 'author', 'title', 'body', 'created_at',
        ]