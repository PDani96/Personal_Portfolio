from django.shortcuts import render

def esl(request):
    return render(request, "projects/esl.html")