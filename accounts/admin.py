from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, UserProfile, Keyword
# Register your models here.
class UserProfileInline(admin.StackedInline):
    model = UserProfile

class CustomUserAdmin(UserAdmin):
    inlines = [UserProfileInline]

admin.site.register(User, CustomUserAdmin)
admin.site.register(Keyword)  # Keyword 모델을 admin 페이지에 등록
