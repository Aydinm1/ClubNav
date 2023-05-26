from rest_framework import serializers
from .models import Club

class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = ('id', 'name', 'description', 'sponsor', 'club_president', 'category', 'meeting_room', 'start_time', 'end_time')