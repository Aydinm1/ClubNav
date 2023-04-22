import random, itertools
from django.shortcuts import render

# Create your views here.
# Request handler - request -> response

from django.http import HttpResponse
from .models import Club
from django.template import loader

def index(request):
    random_clubs = []
    template = loader.get_template("index.html")
    context = {
        "random_clubs": random_clubs,
    }
    for _ in range(3):
        random_club = Club.get_random_club()
        random_clubs.append(random_club)
    return HttpResponse(template.render(context))

