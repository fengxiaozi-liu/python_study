from django.db import models


# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(max_length=32,unique=True)
    password = models.CharField(max_length=64)


class Classes(models.Model):
    title = models.CharField(max_length=16)


class Student(models.Model):
    student_name = models.CharField(max_length=16)
    gender_list = ((1, '男'), (2, '女'))
    gender = models.IntegerField(choices=gender_list)
    cls = models.ForeignKey('Classes', on_delete=models.CASCADE)


class Teacher(models.Model):
    teacher_name = models.CharField(max_length=32)


class TeacherToClass(models.Model):
    tch = models.ForeignKey('Teacher', on_delete=models.CASCADE, related_name='teacher')
    cles = models.ForeignKey('Classes', on_delete=models.CASCADE)
