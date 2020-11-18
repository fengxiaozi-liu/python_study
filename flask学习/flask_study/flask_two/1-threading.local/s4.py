"""
threading.local:
    用字典的形式来实现数据的存储功能
"""
from threading import local, Thread, get_ident
import time

storage = {}


def set(k, v):
    ident = get_ident()
    if ident in storage:
        storage[ident][k] = v
    else:
        storage[ident] = {k: v}


def get(k):
    ident = get_ident()
    return storage[ident][k]


def task(arg):
    set('val', arg)
    print(storage)
    time.sleep(2)
    print(get('val'))


for i in range(10):
    t = Thread(target=task, args=(i,))
    t.start()
