import uuid
from django.db import models

#creating a database model
class Post(models.Model):
    id = models.IntegerField(default=0,primary_key=True) #first column
    title = models.CharField('title', max_length=255) #second column
    text = models.TextField('text', null=True,blank=True) #third column
    
    #function to display the post with it's title
    def __str__(self):
        return self.title