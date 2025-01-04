from django.urls import path
from . import views

urlpatterns = [
    path('', views.chess_game, name='chess_game'),
]
