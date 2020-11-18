"""
threading.local:
    作用：为线程开辟一块空间进行数据存储
    通过字典创建一个类似于threading.local 的功能
"""
from threading import local, Thread, get_ident
import time


person = local()


def task(arg):
    person.value = arg
    time.sleep(2)
    print(person.value)
    # print(get_ident())


for i in range(10):
    t = Thread(target=task, args=(i,))
    t.start()
