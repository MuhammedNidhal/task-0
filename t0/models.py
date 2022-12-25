import uuid
from django.db import models

class Post(models.Model):
    id = models.IntegerField(default=0,primary_key=True)
    title = models.CharField('title', max_length=255)
    text = models.TextField('text', null=True,blank=True)
    
    def __str__(self):
        return self.title