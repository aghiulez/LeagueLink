from django.shortcuts import HttpResponse, render

# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the logs index.")

#This is the simplest view possible in Django. To call the view, we need to map it to a URL - and for this we need a URLconf.
#To create a URLconf in the polls directory, create a file called urls.py.