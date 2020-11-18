from threading import local, Thread, get_ident


def task(arg):
    # person.value = arg
    # time.sleep(2)
    # print(person.value)
    print(get_ident())


for i in range(10):
    t = Thread(target=task, args=(i,))
    t.start()
