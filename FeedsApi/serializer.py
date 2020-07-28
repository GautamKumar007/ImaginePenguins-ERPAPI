from rest_framework import serializers
from UserApi.models import User
from .models import Feed

class FeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feed
        fields = '__all__'
