from threading import local,Thread
import time
# person = local()
person = 0


def task(arg):
    global person
    person = arg
    time.sleep(2)
    print(person)


for i in range(10):
    print(i)
    t = Thread(target=task,args=(i,))
    t.start()