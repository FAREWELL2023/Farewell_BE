from django.contrib import admin
from .models import Question, Answer

# Register your models here.
@admin.register(Question)
class QuestionModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'theme')
    search_fields = ('id',)

@admin.register(Answer)
class AnswerModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'question', 'answer_content','answered_at')
    search_fields = ('id',)
