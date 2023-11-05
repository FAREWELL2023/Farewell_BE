from django.contrib import admin
from django.urls import path, include
from .views import RegisterAPIView, AuthAPIView

app_name = 'accounts'

urlpatterns = [
    path("register/", RegisterAPIView.as_view()), # post - 회원가입
    path("auth/", AuthAPIView.as_view()), # 로그인, 로그아웃, 유저 정보
    
]