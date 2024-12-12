from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class PostDB(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)
    image = models.URLField(max_length=200,blank=True,null= True)
    text = models.TextField(max_length=200,null=True,blank=True)
    reaction_count = models.IntegerField(default=0)  # Counter for reactions
    comments = models.JSONField(default=list)  # Store comments as a list
