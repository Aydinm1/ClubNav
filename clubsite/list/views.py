import random
from django.shortcuts import render

# Create your views here.
# Request handler - request -> response

from django.http import HttpResponse
from .models import Club
# from django.template import loader

latest_id = Club.objects.latest('id')

def index(request):
    random_club = Club.objects.get(id=random.randrange(1, latest_id))
    # template = loader.get_template("list/index.html")
    return HttpResponse("Hello, world. You're at the polls index.")

print(latest_id)