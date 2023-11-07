from django.contrib import admin
from django.urls import path, include
from .views import GetPatchAnswerView, QuesListAPIView, AnswerQuestionView

app_name = 'myfarewell'

urlpatterns = [
    path("", AnswerQuestionView.as_view()),
    path("question/", QuesListAPIView.as_view()),
    path("<int:id>/", GetPatchAnswerView.as_view()),
    
]