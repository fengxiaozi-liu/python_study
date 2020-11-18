import pymysql
from DBUtils.PooledDB import PooledDB

POOL = PooledDB(creator=pymysql,
                maxconnections=6,
                mincached=2,
                maxcached=5,
                maxshared=3,
                blocking=True,
                maxusage=None,
                setsession=[],
                ping=0,
                host='127.0.0.1',
                port=3306,
                user='liu',
                password='lh284259',
                database='python_study',
                charset='utf8'
                )
