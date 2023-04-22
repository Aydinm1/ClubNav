from django.shortcuts import render

# Create your views here.
# Request handler - request -> response

def index(request):
    return render(request, 'index.html')
