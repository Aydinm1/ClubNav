# Create your views here.
# Request handler - request -> response

from django.http import HttpResponse
from .models import Club, SponsorName, Categories
from django.template import loader
from django.shortcuts import get_object_or_404

def index(request):
    clubs = Club.objects.all()
    getCategories = Categories.objects.all()
    template = loader.get_template("index.html")
    context = {
        "clubs": clubs,
        "getCategories": getCategories
    }
    return HttpResponse(template.render(context))

def clubtemplate(request, club_id):
    clubs = get_object_or_404(Club, pk=club_id)
    sponsor = SponsorName.objects.filter(club=club_id)
    context = {
        "club": clubs,
        "sponsor": sponsor
    }
    template = loader.get_template("club-template.html")
    return HttpResponse(template.render(context))
