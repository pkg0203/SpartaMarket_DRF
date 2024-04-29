from django.db import models
from accounts.models import User

# Create your models here.
def file_location(instance, filename, **kwargs):
    file_path = f"{instance.title}-{filename}"
    return file_path

class Product(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to=file_location, null=False, blank=True)