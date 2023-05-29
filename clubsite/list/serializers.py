from rest_framework import serializers
from .models import Club, SponsorName

class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = ('id', 'name', 'description', 'sponsor', 'club_president', 'category', 'meeting_room', 'start_time', 'end_time')

class SponsorNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = SponsorName 
        fields = ('sponsor_name', 'sponsor_email')
