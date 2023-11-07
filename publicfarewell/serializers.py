from rest_framework import serializers
from .models import *

class PublicFarewellSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PublicFarewell
        fields = '__all__'
        read_only_field = ['id','created_at']
        
    image = serializers.ImageField(use_url=True, required=False)