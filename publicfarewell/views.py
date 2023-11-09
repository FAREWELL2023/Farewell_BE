from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets, mixins

from .models import PublicFarewell
from .serializers import PublicFarewellSerializer

from django.shortcuts import get_object_or_404
from .pagination import publicfarewellPagination

from rest_framework import permissions
from rest_framework.permissions import AllowAny

from .permissions import IsAdminOrReadOnly
class publicfarewellViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin,mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = PublicFarewell.objects.all()
    serializer_class = PublicFarewellSerializer
    pagination_class = publicfarewellPagination
    
#권한 설정
class PublicFarewellViewSet(viewsets.ModelViewSet):
    queryset = PublicFarewell.objects.all()
    serializer_class = PublicFarewellSerializer
    permission_classes = [IsAdminOrReadOnly]
    
