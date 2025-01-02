from django.urls import path

from . import views

urlpatterns = [
    path('esl', views.esl, name="esl"),
    path('personal_portfolio', views.personal_portfolio, name="personal_portfolio"),
    path('coding_puzzles', views.coding_puzzles, name="coding_puzzles"),
]