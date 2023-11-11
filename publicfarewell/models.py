from django.db import models

# Create your models here.
from django.db import models
from accounts.models import User
# Create your models here.
def image_upload_path(instance, filename):
    return f'{instance.pk}/[filename]'

class Questions(models.Model):
    question = models.TextField(max_length=500, null=True, blank=True, default='')
    

    def __str__(self):
        return self.question
    
    
    
class PublicFarewell(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='', null=True)
    name = models.CharField(max_length=100, blank=False, null=False, default='질문기본값')
    content = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to=image_upload_path, blank=True, null=True)
    hidden = models.BooleanField(default="False", null=False, blank=False)
    owner = models.BooleanField(default="False",null=False, blank=False)