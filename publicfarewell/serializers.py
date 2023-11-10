from rest_framework import serializers
from .models import *

class PublicFarewellSerializer(serializers.ModelSerializer):
    question_text = serializers.CharField(source='question.question', read_only=True)

    class Meta:
        model = PublicFarewell
        fields = '__all__'
        read_only_field = ['id','created_at','question','hidden']
        
    image = serializers.ImageField(use_url=True, required=False)