from django.db import models

# Create your models here.
from django.db import models
from accounts.models import User
from publicfarewell.models import PublicFarewell
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete

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
    # answer_count = models.IntegerField()
    
    
    def __str__(self):
        return f"Answer by {self.user.username} to '{self.question.text}'"

        # Answer 모델에 대한 post_save signal 핸들러
        # @receiver(post_save, sender=Answer)
        # def update_answer_count(sender, instance, **kwargs):
        #     question = instance.question
        #     question.answer_count = Answer.objects.filter(question=question).count()
        #     question.save()

        # # Answer 모델에 대한 post_delete signal 핸들러
        # @receiver(post_delete, sender=Answer)
        # def update_answer_count_on_delete(sender, instance, **kwargs):
        #     question = instance.question
        #     question.answer_count = Answer.objects.filter(question=question).count()
        #     question.save()
    
class Ending(models.Model):
    questions = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_content = models.ForeignKey(Answer, on_delete=models.CASCADE)
    progress_rate = models.IntegerField(default=0, null=False, blank=False)
    
    #남이써준회고록질문+응답
    # 남이 써준 회고록 질문+응답
    public_questions = models.ForeignKey(PublicFarewell, on_delete=models.CASCADE, related_name='ending_public_questions')
    public_name = models.ForeignKey(PublicFarewell, on_delete=models.CASCADE, related_name='ending_public_name')
    public_content = models.ForeignKey(PublicFarewell, on_delete=models.CASCADE, related_name='ending_public_content')
    public_image = models.ForeignKey(PublicFarewell, on_delete=models.CASCADE, related_name='ending_public_image')
    
    
    
    def __str__(self):
        return self.questions.text