import re
from redis import Redis

coon = Redis(host='127.0.0.1', port=6379)
movie_list = coon.lrange('movie_data', 0, -1)
fp = open('../01-requests模块的学习/电影.txt', 'w', encoding='utf-8')
for each in movie_list:
    x = eval(str(each, encoding='utf-8'))
    fp.write(x['name']+'\n'+x['desc']+'\n'+'\n')

fp.close()