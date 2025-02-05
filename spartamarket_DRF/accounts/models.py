from django.db import models
from django.contrib.auth.models import AbstractUser
from products.models import Product
# Create your models here.


class User(AbstractUser):
    class GenderChoices(models.TextChoices):
        MALE = 'M', '남성'
        FEMALE = 'F', '여성'
    email = models.EmailField(unique=True)
    nickname = models.CharField(max_length=50, blank=False)
    birthday = models.DateField(blank=False)
    gender = models.CharField(
        choices=GenderChoices.choices, max_length=1, blank=True)
    self_introduction = models.TextField(blank=True)
    like = models.ManyToManyField(
        Product, 
        related_name="liked", 
        symmetrical=False
    )
    follow = models.ManyToManyField(
        "self", 
        related_name="follower", 
        symmetrical=False
    )
