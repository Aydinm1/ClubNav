import random, itertools
from django.shortcuts import render

# Create your views here.
# Request handler - request -> response

from django.http import HttpResponse
from .models import Club
from django.template import loader


def index(request):   
    template = loader.get_template("list/index.html")
    return HttpResponse("Hello, world. You're at the polls index.")
