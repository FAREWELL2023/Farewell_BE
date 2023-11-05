# serializers.py

from .models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)  # 패스워드 확인용 필드

    class Meta:
        model = User
        fields = '__all__'
        
    def create(self, validated_data):
        # 패스워드와 패스워드 확인 필드의 값을 가져옴
        password = validated_data.get('password')
        password2 = validated_data.pop('password2', None)  # 'password2' 필드를 validated_data에서 제거

        # 패스워드 확인 필드와 일치하는지 확인
        if password != password2:
            raise serializers.ValidationError("패스워드가 일치하지 않습니다.")

        # 나머지 필드로 사용자 생성
        # user = User.objects.create_user(**validated_data)
        user = User.objects.create_user(
            username = validated_data['username'],
            email = validated_data['email'],
            password = password
        )
        return user
