from django.db import models

# Create your models here.
class PublicFarewell(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)
    content = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)