from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets, mixins

from .models import PublicFarewell
from .serializers import PublicFarewellSerializer

from django.shortcuts import get_object_or_404


class publicfarewellViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin,mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = PublicFarewell.objects.all()
    serializer_class = PublicFarewellSerializer