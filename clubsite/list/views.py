# Create your views here.
# Request handler - request -> response

from django.http import HttpResponse
from .models import Club
from django.template import loader

def index(request):
    random_clubs = Club.objects.filter(name="Interact")
    template = loader.get_template("index.html")
    context = {
        "random_clubs": random_clubs,
    }
    return HttpResponse(template.render(context))

def clubtemplate(request):
    template = loader.get_template("club-template.html")
    return HttpResponse(template.render())
