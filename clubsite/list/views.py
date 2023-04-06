from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    template = loader.get_template("list/index.html")
    return HttpResponse("Hello, world. You're at the polls index.")
