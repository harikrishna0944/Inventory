# Create your models here.
from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    quantity = models.IntegerField(default=0)
    

    def __str__(self):
        return self.name

