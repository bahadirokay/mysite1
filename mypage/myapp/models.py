from django.db import models
from datetime import datetime

# Create your models here.

class list_todo(models.Model):
    title = models.CharField(blank=True, max_length=100)
    aciklama = models.TextField(max_length=1000)
    date = models.DateField(default = datetime.now, blank=True)
    finished = models.BooleanField(default= False)


    def __str__(self):
        return (self.title)


