from django.db import models
from django.contrib.auth.models import User 
# Create your models here.

class ChatsDB(models.Model):
    user1 = models.OneToOneField(User,on_delete=models.CASCADE,related_name="pk")
    user2 = models.IntegerField()

class MessageDB(models.Model):
    chat = models.ManyToManyField(ChatsDB)
    owner = models.OneToOneField(User,on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)