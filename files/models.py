from django.db import models
from common.models import BaseModel


# Create your models here.
class Document(BaseModel):
    title = models.CharField(max_length=200)
    content = models.TextField

    img = models.ImageField(upload_to='images/')
    files = models.FileField(upload_to='files/')
    video = models.FileField(upload_to='video/')

