from rest_framework import serializers
from .models import *

class PublicFarewellSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PublicFarewell
        fields = '__all__'