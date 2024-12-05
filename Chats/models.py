from django.db import models
from django.contrib.auth.models import User 
# Create your models here.

class ChatsDB(models.Model):
    user1 = models.OneToOneField(User,on_delete=models.PROTECT)
    user2 = models.OneToOneField(User,on_delete=models.PROTECT)

class MessageDB(models.Model):
    chat = models.ManyToOneRel(ChatsDB,on_delete=models.CASCADE)
    owner = models.OneToOneRel(User,on_delete=models.PROTECT)
    create_date = models.DateTimeField(auto_now_add=True)