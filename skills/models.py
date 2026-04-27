from django.db import models

# Create your models here.
class Skills(models.Model):
    name = models.CharField(max_length=100)
    descriptions = models.TextField()
    price = models.IntegerField()