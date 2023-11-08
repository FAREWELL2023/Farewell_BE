from django.contrib import admin
from .models import Questions, PublicFarewell 

# Register your models here.
@admin.register(Questions)
class QuestionsModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', )
    search_fields = ('id',)

@admin.register(PublicFarewell)
class PublicFarewellModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'question', 'name','content', 'created_at', 'image')
    search_fields = ('id',)