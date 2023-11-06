from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import PublicFarewell
from .serializers import PublicFarewellSerializer

from django.shortcuts import get_object_or_404


@api_view(['GET', 'POST'])
def PublicFarewell_list_create(request):
    
    if request.method == 'GET':
        publicfarewells = PublicFarewell.objects.all()
        serializer = PublicFarewellSerializer(publicfarewells, many=True)
        return Response(data=serializer.data)
    
    
    if request.method == 'POST':
        serializer = PublicFarewellSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data)