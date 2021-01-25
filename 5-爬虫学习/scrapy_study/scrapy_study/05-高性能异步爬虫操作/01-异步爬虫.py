"""
异步爬虫：
    多线程爬取数据
异步爬虫的方式：
    -多线程或者多进程进行爬取操作(不建议使用，后面有更好的方案)：
        优点：可以为相关阻塞的操作单独的开启线程或者进程，阻塞就可以异步执行
        缺点： 无法无限制的开启多线程或者多进程
    -线程池或者进程池(适当的使用)
        优点：可以降低系统对进程或者线程创建和销毁的频率，从而很好的降低系统的开销
        缺点：池中的线程或者进程的数量是有上限的
    线程池的基本使用
"""
import time
from multiprocessing.dummy import Pool

start_time = time.time()


def get_page(str):
    print('正在下载', str)
    time.sleep(2)
    print('下载成功', str)


name_list = ['zhangsan', 'lisi', 'wangwu']

pool = Pool(4)

pool.map(get_page, name_list)

end_time = time.time()
print(end_time-start_time)
