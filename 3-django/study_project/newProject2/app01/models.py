from django.db import models
from django.core.validators import RegexValidator
from django.core.validators import DecimalValidator


# Create your models here.

class UserInfo(models.Model):
    username = models.CharField(max_length=32)
    email = models.EmailField()
    f = models.FileField(default=11)
    ctime = models.DateTimeField(null=True)
    color_list = [
        (1, '黑色'), (2, '白色'), (3, '蓝色')
    ]
    color = models.IntegerField(color_list, default=1)
    test = models.CharField(
        max_length=32,
        error_messages={'c1': '优先错误'},
        validators=[
            RegexValidator(regex=r'root_\d+', message='错误了', code='c1')
        ],
        null=True

    )


class UserList(models.Model):
    username = models.CharField(max_length=16)
    passwd = models.CharField(max_length=32)
