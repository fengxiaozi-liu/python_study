from django.db import models


# Create your models here.

class Department(models.Model):
    """
    部门表
    """
    title = models.CharField(verbose_name='部门', max_length=32)

    def __str__(self):
        return self.title


class UserInfo(models.Model):
    """
    用户表
    """
    name = models.CharField(verbose_name='用户名', max_length=16)
    age = models.IntegerField(verbose_name='用户年龄')
    gender = models.IntegerField(verbose_name='性别', choices=((1, '男'), (2, '女')))
    email = models.EmailField(verbose_name='邮箱', max_length=64)
    depart = models.ForeignKey(verbose_name='所属部门', to='Department', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
