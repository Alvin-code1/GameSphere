from django.db import models
from Profile.models import PRofileDB
# Create your models here.

class PostDB(models.Model):
    profile = models.OneToOneField(PRofileDB, on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(blank=True,null= True)
    text = models.TextField(max_length=200,null=False,blank=False)