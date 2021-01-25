from django.db import models


# Create your models here.


class AbstractDefaultColumn(models.Model):
    date1 = models.DateTimeField(auto_now_add=True)
    date2 = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Professional(AbstractDefaultColumn):  # 艺术家
    penname = models.CharField(max_length=255, default='')  # 笔名
    hot_score = models.PositiveIntegerField(default=0)  # 热度


class Attention(AbstractDefaultColumn):  # 粉丝
    professional = models.ForeignKey(Professional, related_name='attention_pro', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default='')  # 昵称
