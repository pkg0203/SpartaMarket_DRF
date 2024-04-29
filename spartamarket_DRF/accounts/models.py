from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    class GenderChoices(models.TextChoices):
        MALE = 'M', '남성'
        FEMALE = 'F', '여성'
    nickname = models.CharField(max_length=50,blank=False)
    birthday = models.DateField(blank=False)
    gender = models.CharField(choices=GenderChoices.choices, max_length=1,blank=True)
    self_introduction = models.TextField(blank=True)