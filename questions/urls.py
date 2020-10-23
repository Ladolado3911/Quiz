from django.urls import path
from . import views


app_name = 'questions'

urlpatterns = [
    path('', views.home_page, name = "home_page"),
    path('quiz/', views.quiz, name = "quiz1"),
    path('next/', views.next_question, name = "next")
]