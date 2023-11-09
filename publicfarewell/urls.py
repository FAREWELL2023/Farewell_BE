from django.urls import path, include
from rest_framework import routers
from .views import *
from . import views



app_name="publicfarewell"

default_router = routers.SimpleRouter()
default_router.register("",publicfarewellViewSet, basename="publicfarewell")
urlpatterns = [
    path("",include(default_router.urls)),
]
