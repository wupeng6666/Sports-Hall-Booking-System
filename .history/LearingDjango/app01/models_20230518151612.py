from django.db import models
# 专门对数据库操作，重要
# Create your models here.
class UserInfo(models.Model):
    name=models.CharField(max_length=32)
    password=models.CharField(max_length=64)
    name=models.CharField(max_length=32)