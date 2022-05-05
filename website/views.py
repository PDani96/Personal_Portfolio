from django.shortcuts import render

def home(request):
    return render(request, "website/home.html")

def resume(request):
    return render(request, "website/resume.html")