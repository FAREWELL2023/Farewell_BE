from django.db import models

# Create your models here.
from django.db import models
from accounts.models import User
from publicfarewell.models import PublicFarewell

# def image_upload_path(instance, filename):
#     return f'{instance.pk}/[filename]'


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

class Ending(models.Model):
    questions = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_content = models.ForeignKey(Answer, on_delete=models.CASCADE)
    progress_rate = models.IntegerField(default='0%', null=False, blank=False)
    
    #남이써준회고록질문+응답
    # 남이 써준 회고록 질문+응답
    public_questions = models.ForeignKey(PublicFarewell, on_delete=models.CASCADE, related_name='ending_public_questions')
    public_name = models.ForeignKey(PublicFarewell, on_delete=models.CASCADE, related_name='ending_public_name')
    public_content = models.ForeignKey(PublicFarewell, on_delete=models.CASCADE, related_name='ending_public_content')
    public_image = models.ForeignKey(PublicFarewell, on_delete=models.CASCADE, related_name='ending_public_image')