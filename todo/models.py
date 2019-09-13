from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
 
    body = models.CharField(max_length=200)
    
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    created_on=models.DateField('created on')
    def __str__(self):
        return self.body
    class order:
        ordering = ['-created_on']
