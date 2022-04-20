from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse

from meetings.models import Meeting

def home(request):
    return render(request, "website/home.html")

def date(request):
    return HttpResponse("This page was served at " + str(datetime.now()))

def about(request):
    return HttpResponse("Hi! My name is Preston Danielson. I am an Electrical and Software Engineer based in Dallas, Texas.")