from django.shortcuts import render

# Create your views here.
# Request handler - request -> response

from django.http import HttpResponse
# from django.template import loader
# Deciding whether or not to use the template system 


def index(request):
    # template = loader.get_template("list/index.html")
    return HttpResponse("Hello, world. You're at the polls index.")
