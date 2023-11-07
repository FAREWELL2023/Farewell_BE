from django.db import models

# Create your models here.
from django.db import models
from accounts.models import User

class Question(models.Model):
    text = models.CharField(max_length=200, default='')
    theme = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.text

class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_content = models.TextField(max_length=500,null=True,blank=True)  # 사용자의 답변
    answered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Answer by {self.user.username} to '{self.question.text}'"
