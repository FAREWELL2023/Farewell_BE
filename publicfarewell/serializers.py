from rest_framework import serializers
from .models import *
from publicfarewell.models import*

class PublicFarewellSerializer(serializers.ModelSerializer):
    question_text = serializers.CharField(source='question.question', read_only=True)
    owner = serializers.BooleanField(read_only=True)

    class Meta:
        model = PublicFarewell
        fields = '__all__'
        read_only_field = ['id','created_at','question','hidden','owner']
        
    image = serializers.ImageField(use_url=True, required=False)
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get('request', None)

        # Check if the request is available and the user is authenticated
        if request and request.user.is_authenticated:
            # Add the 'owner' field to the response data
            data['owner'] = instance.owner

        return data



class PublicFarewellSerializer(serializers.ModelSerializer):
    question_text = serializers.CharField(source='question.question', read_only=True)
    owner = serializers.BooleanField(read_only=True)



    class Meta:
        model = PublicFarewell
        fields = '__all__'
        read_only_field = ['id','created_at','question','hidden','owner']
        
    image = serializers.ImageField(use_url=True, required=False)
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get('request', None)

        # Check if the request is available and the user is authenticated
        if request and request.user.is_authenticated:
            # Add the 'owner' field to the response data
            data['owner'] = instance.owner

        return data
class PublicFarewellSerializer(serializers.ModelSerializer):
    question_text = serializers.CharField(source='question.question', read_only=True)

    class Meta:
        model = PublicFarewell
        fields = '__all__'
        read_only_field = ['id','created_at','question','hidden','owner']
        
    image = serializers.ImageField(use_url=True, required=False)
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get('request', None)

        # Check if the request is available and the user is authenticated
        if request and request.user.is_authenticated:
            # Add the 'owner' field to the response data
            data['owner'] = instance.owner

        return data
