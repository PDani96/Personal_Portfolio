from django.urls import path

from . import views

urlpatterns = [
    path('esl', views.esl, name="esl"),
]