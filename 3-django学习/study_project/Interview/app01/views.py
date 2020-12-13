from django.shortcuts import render, HttpResponse
from app01 import models
from django.db.models import Q, F, Count
import json
from time import ctime

'''
查询艺术家：（请求参数：name=厘米&limit=20&offset=0）
①	艺术家笔名或者其粉丝的昵称包含“厘米”
②	按照艺术家的粉丝数由高到低排序
③	根据前端传的limit、offset参数分页
④	响应json格式，响应参数包括每个艺术家的id、笔名、创建时间（东八区），
        以及本页所有艺术家的热度之和
⑤	所有查询出的艺术家，将其热度加1
'''


# Create your views here.

def a_view(request):
    # =================第一题,第二题和第三题===============
    profession_list = models.Professional.objects.filter(
        Q(penname__contains='厘米') | Q(attention_pro__name__contains='厘米')).values('id', 'penname',
        'hot_score', 'date1').annotate(attention_nums=Count('attention_pro')).order_by('-attention_nums')[0:20]
    return_list = []
    total_hot_scores = 0
    # ===========================第四题===========================
    for every in profession_list:
        total_hot_scores += every['hot_score']
        temp = {'id': every['id'], 'penname': every['penname'], 'time': ctime(every['date1'])}
        return_list.append(temp)
    return_list.append(total_hot_scores)
    print(return_list)
    value = json.dumps(return_list)
    # ==============第五题================
    models.Professional.objects.filter(
        Q(penname__contains='厘米') | Q(attention_pro__name__contains='厘米')).update(hot_score=F('hot_score') + 1)

    return HttpResponse(value)
