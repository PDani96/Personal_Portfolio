from django.shortcuts import render

def esl(request):
    return render(request, "projects/esl.html")

def personal_portfolio(request):
    return render(request, "projects/personal_portfolio.html")

def coding_puzzles(request):
    return render(request, "projects/coding_puzzles.html")