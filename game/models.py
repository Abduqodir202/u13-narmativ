from django.db import models

# Create your models here.
from django.db import models

class Game(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.name