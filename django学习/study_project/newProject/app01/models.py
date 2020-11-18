from django.db import models


# Create your models here.


class UserType(models.Model):
    title = models.CharField(max_length=32)


class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    ut = models.ForeignKey('UserType', on_delete=models.CASCADE)


class Boy(models.Model):
    name = models.CharField(max_length=32)
    # 创建一个外键，连接Girl，且不生成新的表，就通过Love表去连接,连接的是关联的字段分别是b,g
    m = models.ManyToManyField('Girl', through='Love', through_fields=('b', 'g'))


class Girl(models.Model):
    nick = models.CharField(max_length=32)


class Love(models.Model):
    b = models.ForeignKey('Boy', on_delete=models.CASCADE)
    g = models.ForeignKey('Girl', on_delete=models.CASCADE)
    time = models.DateTimeField(null=True)
    # 做联合唯一索引
    # class Meta:
    #     unique_together = [('b', 'g')]
