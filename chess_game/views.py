from django.shortcuts import render

def chess_game(request):
    return render(request, 'chess_game/chess_game.html')
