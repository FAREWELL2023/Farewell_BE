from django.urls import path
from .views import *
from . import views



app_name="publicfarewell"
urlpatterns = [
    path('', views.PublicFarewell_list_create),
]
