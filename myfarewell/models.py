from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    text = models.CharField(max_length=200, unique=True) 
    available_after = models.DateField()  # 답변 가능한 날짜??....

    def __str__(self):
        return self.text

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) 
    answer_content = models.TextField(max_length=500,null=False,blank=False)  # 사용자의 답변
    answered_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f"Answer by {self.user.username} to '{self.question.text}'"
