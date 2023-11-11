from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from .views import GetPatchAnswerView, QuesListAPIView, AnswerQuestionView, EndingListView

app_name = 'myfarewell'


urlpatterns = [
    path("", AnswerQuestionView.as_view()),
    path("question/", QuesListAPIView.as_view()),
    path("<int:id>/", GetPatchAnswerView.as_view()),
    path("ending/", EndingListView.as_view(), name='ending_list'),

]