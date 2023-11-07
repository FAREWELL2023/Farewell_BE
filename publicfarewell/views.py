from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets, mixins

from .models import PublicFarewell
from .serializers import PublicFarewellSerializer

from django.shortcuts import get_object_or_404
from .pagination import publicfarewellPagination

from rest_framework import permissions

class publicfarewellViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin,mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = PublicFarewell.objects.all()
    serializer_class = PublicFarewellSerializer
    pagination_class = publicfarewellPagination
    
    def get_permissions(self):
        if self.action == 'destroy' or self.action == 'update':
            # 삭제 또는 업데이트 작업을 수행하는 경우에만 권한을 확인합니다.
            return [permissions.IsAuthenticated, IsOwnerOrReadOnly()]
        return [permissions.AllowAny]
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True  # 안전한 메서드 (읽기)에 대해서는 항상 허용
        # 삭제 또는 업데이트 작업을 수행하려면 사용자가 피드의 소유자인지 확인
        return obj.owner == request.user