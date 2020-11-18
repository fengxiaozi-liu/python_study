try:
    from greenlet import getcurrent as get_ident
except Exception as e:
    from threading import get_ident
from threading import Thread
import time


class Local:

    def __init__(self):
        object.__setattr__(self, 'storage', {})

    def __setattr__(self, key, value):
        ident = get_ident()
        if ident in self.storage:
            self.storage[ident][key] = value
        else:
            self.storage[ident] = {key: value}

    def __getattr__(self, key):
        ident = get_ident()
        return self.storage[ident][key]


obj = Local()


def task(arg):
    obj.val = arg
    print(obj.storage)
    time.sleep(2)
    print(obj.val)


for i in range(10):
    t = Thread(target=task, args=(i,))
    t.start()
