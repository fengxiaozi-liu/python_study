from django.db import models


# Create your models here.

class UserInfo(models.Model):
    username = models.CharField(max_length=8)
    password = models.CharField(max_length=16)
