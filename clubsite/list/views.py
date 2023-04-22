# Create your views here.
# Request handler - request -> response

from django.http import HttpResponse
from .models import Club
from django.template import loader

def index(request):
    random_clubs = Club.get_random_club()
    template = loader.get_template("index.html")
    context = {
        "random_clubs": random_clubs,
    }
    return HttpResponse(template.render(context))

