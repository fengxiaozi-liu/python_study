"""
需求：
request.get 是基于同步的，必须使用基于异步的网络请求模块进行指定url的请求发送
aiohttp: 基于异步网络请求的模块
    使用方式：
        1.下载相关的环境
        2.使用这个模块中的ClientSession类实例化一个session对象
        async with aiohttp.ClientSession() as session:
            async await with session.get(url) as response:  这里代理的参数变成了proxy 不是proxies
                page_text = await response.text()/read()/json  在获取响应数据之前一定要手动挂起
                    text() 返回的字符串类型的数据
                    read() 返回的是一个二进制类型的数据
                    json() 返回的是一个json对象

"""
import asyncio
import time
import aiohttp

urls = ['http://127.0.0.1:5000/index', 'http://127.0.0.1:5000/demo', 'http://127.0.0.1:5000/func']

start = time.time()


async def get_page(url):
    # print('正在下载', url)
    # # request.get 是基于同步的，必须使用基于异步的网络请求模块进行指定url的请求发送
    # response = requests.get(url=url).text
    # print(response)
    async with aiohttp.ClientSession() as session:
        # 手动挂起阻塞操作
        async with session.get(url) as response:
            # text()是返回字符串类型的相应数据
            # read() 返回的是一个二进制类型的响应数据
            # json  返回的是一个json对象
            # 在拿到页面之前对响应的数据进行一次挂起
            page_text = await response.text()
            print(page_text)

tasks = []

for url in urls:
    c = get_page(url)
    task = asyncio.ensure_future(c)
    tasks.append(task)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
print(time.time()-start)
