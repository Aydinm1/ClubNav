# Create your views here.
# Request handler - request -> response

from rest_framework import viewsets
from .serializers import ClubSerializer
from django.http import HttpResponse
from .models import Club, SponsorName, Categories, MeetingRooms
from django.template import loader
from django.shortcuts import get_object_or_404

class ClubViewSet(viewsets.ModelViewSet):
    serializer_class = ClubSerializer
    queryset = Club.objects.all()

def clubtemplate(request, club_id):
    clubs = get_object_or_404(Club, pk=club_id)
    sponsors = SponsorName.objects.filter(club=club_id)
    meeting_room = MeetingRooms.objects.filter(club=club_id)
    context = {
        "club": clubs,
        "sponsors": sponsors,
        "meeting_room": meeting_room
    }
    template = loader.get_template("club-template.html")
    return HttpResponse(template.render(context))
