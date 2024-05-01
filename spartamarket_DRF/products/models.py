from django.db import models
from django.conf import settings
# Create your models here.


def file_location(instance, filename, **kwargs):
    file_path = f"{instance.title}-{filename}"
    return file_path


class Product(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to=file_location, null=False, blank=True)
