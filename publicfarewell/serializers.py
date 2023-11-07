from rest_framework import serializers
from .models import *

class PublicFarewellSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PublicFarewell
        fields = '__all__'
        
    image = serializers.ImageField(use_url=True, required=False)