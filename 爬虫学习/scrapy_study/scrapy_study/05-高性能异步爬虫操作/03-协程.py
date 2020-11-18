"""
单线程+异步协程：
    event_loop:
        事件循环，相当于一个无限循环，可以把一些函数注册到这个事件循环上，
        当满足某些条件的时候，函数就会被循环执行。
    coroutine：
        协程对象，可以将协程对象注册到事件循环中，它会被事件循环调用。我们可以使用
        async关键字定义一个方法，这个方法在调用的时候不会立即被执行，而是返回一个协程对象
    task:
        任务，它是对协程对象的进一步封装，包含了任务的各个状态
    future:
        代表将来执行或没有执行的任务，实际上和task没有本质区别
    async：
        定义一个协程
    await：
        用来挂起阻塞方法执行
    回调函数：
        任务对象.add_done_callback(函数): 用来绑定一个任务对象
        task.result() 的返回值是任务对象封装的协程对象对应函数的返回值
"""

# 协程的实现
import asyncio


# 用async修饰函数，调用之后返回的是一个协程对象
async def request(url):
    print('正在请求的url', url)
    return '请求成功'


# 创建一个协程对象
c = request('www.baidu.com')


# # 创建一个一个事件循环对象
# loop = asyncio.get_event_loop()
#
# # 将协程对象注册到事件循环对象中
# loop.run_until_complete(c)

# task的使用
# loop = asyncio.get_event_loop()
# # 基于loop创建一个task对象
# task1 = loop.create_task(c)
# print(task1)
# loop.run_until_complete(task1)

# # future的使用
# loop = asyncio.get_event_loop()
# future = asyncio.ensure_future(c)
# print(future)
# loop.run_until_complete(future)

# 绑定回调
# 回调函数
def callback_func(task):
    # result返回的就是任务对象中封装的协程对象对应函数的返回值
    print(task.result())


loop = asyncio.get_event_loop()
task = asyncio.ensure_future(c)
print(task)
# 将回调函数绑定到任务对象中
task.add_done_callback(callback_func)
loop.run_until_complete(task)
