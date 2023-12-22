from django.db import models

# Create your models here.


class Gym(models.Model):
    gym_name = models.CharField(verbose_name='场馆名', max_length=64, primary_key=True)
    max_people = models.IntegerField(verbose_name="最大人数")

class Student(models.Model):
        # 学生表
    student_name = models.CharField(verbose_name='姓名', max_length=32,unique=True)
    student_chances = models.IntegerField(verbose_name="剩余次数")
    student_number = models.BigIntegerField(verbose_name="学号", primary_key=True)


class Comeing_time(models.Model):
    yuyue_time = models.CharField(max_length=20, verbose_name='预约时间')
    yueye_xingqi = models.CharField(max_length=20, verbose_name='预约日期')
    gym_name = models.ForeignKey(Gym, on_delete=models.CASCADE, verbose_name='场馆名称')
    student_name = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='学生姓名', related_name='comeing_time_by_name')
    student_number = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='学号', related_name='comeing_time_by_number')
    now_people = models.IntegerField(default=1, verbose_name='当前人数')
    #max_people = models.IntegerField(Gym, on_delete=models.CASCADE,verbose_name='最大容量')


