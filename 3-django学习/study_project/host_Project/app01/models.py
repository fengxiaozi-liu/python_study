from django.db import models
from rbac.models import UserInfo as RbacUserInfo


# Create your models here.

class Department(models.Model):
    title = models.CharField(verbose_name='部门', max_length=32)

    def __str__(self):
        return self.title


class UserInfo(RbacUserInfo):
    phone = models.CharField(verbose_name='手机号', max_length=32)

    level_choices = [(1, 't1'), (2, 't2'), (3, 't3')]

    level = models.IntegerField(choices=level_choices)

    depart = models.ForeignKey(verbose_name='所属部门', to='Department', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.name


class Host(models.Model):
    hostname = models.CharField(verbose_name='主机名', max_length=32)
    ip = models.GenericIPAddressField(verbose_name='IP', max_length=64)

    depart = models.ForeignKey(verbose_name='所属部门', to='Department', on_delete=models.CASCADE)

    def __str__(self):
        return self.hostname
