from django.shortcuts import render

def home(request):
    return render(request, "website/home.html")

def resume(request):
    return render(request, "website/resume.html")

def esl(request):
    return render(request, "projects/esl.html")

def personal_portfolio(request):
    return render(request, "projects/personal_portfolio.html")

def coding_puzzles(request):
    return render(request, "projects/coding_puzzles.html")