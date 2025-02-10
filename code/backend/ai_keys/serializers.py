from ai_keys.models import AiKey
from rest_framework import serializers

class AiKeyCreateSerializer(serializers.ModelSerializer):
    api_key = serializers.CharField(read_only=True, source='raw_key')
    class Meta:
        model = AiKey
        fields = ['id', 'created_at', 'api_key']
        read_only_fields = ['id', 'created_at', 'api_key']


    
