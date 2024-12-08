from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class PRofileDB(models.Model):
    username = models.TextField(verbose_name='Username',max_length=30,null=False,blank=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    url = models.URLField(null=True,blank=True)
    # profile_pic = models.ImageField(null=True, blank=True)
    # back_profile_pic = models.ImageField(null=True,blank=True)
    description = models.TextField(null=True,default="empty",blank=True)
