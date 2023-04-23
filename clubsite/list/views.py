# Create your views here.
# Request handler - request -> response

from django.http import HttpResponse
from .models import Club
from django.template import loader
from django.shortcuts import get_object_or_404

def index(request):
    random_clubs = Club.get_random_club()
    template = loader.get_template("index.html")
    context = {
        "random_clubs": random_clubs,
    }
    return HttpResponse(template.render(context))

def clubtemplate(request, club_id):
    clubs = get_object_or_404(Club, pk=club_id)
    context = {
        "club": clubs
    }
    template = loader.get_template("club-template.html")
    return HttpResponse(template.render(context))
