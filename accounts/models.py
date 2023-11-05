from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver

from .managers import UserManager

class User(AbstractUser):

    username = models.CharField(max_length=64, verbose_name="사용자이름", unique=False)
    email = models.EmailField(_('email address'), unique=True)

    # is_superuser = models.BooleanField(default=False)
    # is_active = models.BooleanField(default=True)
    # is_staff = models.BooleanField(default=False)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

class Keyword(models.Model):
    keyword = models.CharField(max_length=255, unique=True)
    def __str__(self):
        return self.keyword

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    keywords = models.ManyToManyField(Keyword)
    def __str__(self):
        return ', '.join([keyword.keyword for keyword in self.keywords.all()])


