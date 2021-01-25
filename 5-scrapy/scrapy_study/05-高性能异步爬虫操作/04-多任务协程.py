"""
基于多任务的协程：
    在异步协程中如果出现了同步模块相关的代码，就无法实现异步
    在asyncio中遇到阻塞操作， 必须进行手动挂起: 实现挂起的方式就是用await关键字进行挂起
"""

import asyncio
import time

start = time.time()
async def request(url):
    print('正在下载', url)
    # 在asyncio中遇到阻塞操作， 必须进行手动挂起
    await asyncio.sleep(2)
    return '下载完毕'


urls = ['www.baidu.com', 'www.sougou.com', 'www.google.com']


# 绑定回调函数
def call_back(task):
    print(task.result())


# 多任务要用到任务列表存放多个任务对象
stasks = []
for url in urls:
    c = request(url)
    task = asyncio.ensure_future(c)
    task.add_done_callback(call_back)
    stasks.append(task)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(stasks))
print(time.time()-start)
