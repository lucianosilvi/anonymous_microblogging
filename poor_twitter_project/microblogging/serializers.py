from rest_framework import serializers
from .models import *


class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = '__all__'
    
    time = serializers.SerializerMethodField()

    def get_time(self, obj):
        return obj.time.strftime("%Y-%m-%d %H:%M:%S")
