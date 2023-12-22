from django.db import models
# 专门对数据库操作，重要
# Create your models here.
class UserInfo(models.Model):
    name=models.CharField(max_length=32)
    pass=models.CharField(max_length=32)
    name=models.CharField(max_length=32)