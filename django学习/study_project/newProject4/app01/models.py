from django.db import models


# Create your models here.

class UserInfo(models.Model):
    nickname = models.CharField(max_length=32)
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    gender_choice = (
        (1, '男'),
        (2, '女'),
    )
    gender = models.IntegerField(choices=gender_choice)
    m = models.ManyToManyField('UserInfo')


# class UToU(models.Model):
#     # 因为外键在同一张表里面，不能实现反向查找，引入related_query_name来定义反向查找的名字
#     # 加上related_query_name之后反向查找就由表名小写_set 变成了 a_set
#     # g = models.ForeignKey('UserInfo', related_query_name='a')
#     # b = models.ForeignKey('UserInfo', related_query_name='b')
#
#     # 用related_name更加简单，反向查找的时候直接写a，related_name定义反向查找的名字
#     # 定义了反向查找的名字之后，反向查找就由表名小写_set 变成了 a
#     g = models.ForeignKey('UserInfo', related_name='girl', on_delete=models.CASCADE)
#     b = models.ForeignKey('UserInfo', related_name='boy', on_delete=models.CASCADE)


class Comment(models.Model):
    """
    评论表
    """
    news_id = models.IntegerField()  # 新闻id
    content = models.CharField(max_length=32)  # 评论的内容
    user = models.CharField(max_length=32)  # 评论者
    reply = models.ForeignKey('Comment', null=True, blank=True, on_delete=models.CASCADE)
