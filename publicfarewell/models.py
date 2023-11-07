from django.db import models
from django.contrib.auth.models import User
# Create your models here.
def image_upload_path(instance, filename):
    return f'{instance.pk}/[filename]'

class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=15, null=True, blank=True)

class PublicFarewell(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)
    content = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to=image_upload_path, blank=True, null=True)
    questions = models.TextField(max_length=500, null=True, blank=True)
    tag = models.ManyToManyField(Tag, blank=True)
    owner = models.ForeignKey(accounts.AUTH_USER_MODEL, on_delete=models.CASCADE)
