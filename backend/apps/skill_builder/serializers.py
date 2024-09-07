from rest_framework import serializers
from .models import TopicFather

class TopicFatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopicFather
        fields = ['id', 'topic_father']
