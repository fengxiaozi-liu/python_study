"""
scrapy框架
    什么是框架：
        集成了很多功能并且具有很强通用性的一个项目模板
    如何学习框架：
        专门学习框架的各种功能的详细用法，熟练之后再对相关的源码进行解析
    什么是scrapy：
        爬虫中封装好的一个明星框架
            -封装的功能
                高性能的持久化操作
                异步的数据下载
                高性能的数据解析
                分布式
            -详细用法
scrapy框架的基本的使用
    环境安装：
        mac或者linux  pip install scrapy
    windows:
        1.pip install wheel
        2.下载twisted
        3.安装twisted
        4.pip install pywin32
        5.pip install scrapy
    创建一个工程：
        scrapy startproject xxProject
        在spiders子目录中创建一个爬虫文件
            scrapy genspider spiderName www.xxx.com
        执行工程
            scrapy crawl spiderName

-scrapy数据解析：
    div_list = response.xpath('//div[@id="content"]/div/div[2]/div') 直接使用response进行解析

-scrapy持久化存储
    1.基于终端命令的持久化
        要求：只可以将parse方法的返回值存储到本地文本文件中
        注意：持久化存储对应的文本文件的类型只能是json， jsonlines， jl， csv， xml, marshal, pickle
        指令：scrapy crawl name -o filePath
        好处：简介高效便捷
        缺点：局限性比较强(数据只可以存储到指定后缀的文本文件中)
    2.基于管道：
        编码流程：
            1.数据解析
            2.在item类中定义相关的属性
            2.将数据对象封装存储到item类型的对象中
            4.将item类型的对象提交给管道进行持久化存储的操作
            5.在管道类的process_items中将要接收到的item对象中存储的数据进行持久化存储操作
            6.在配置文件中开启管道
        优点：通用性强
        缺点：框架大，繁琐
    3.面试题：将爬取的数据一份存储到本地，一份存储到数据库
        再建立一个管道类用来将数据写入到数据库中
        爬虫文件的item只会给一个管道文件中第一个被执行的管道类接收
        后续想要获得item要返回item
基于Spider的全站爬取
    -就将网站中某板块下的全部页码对应页面数据进行爬取
    -爬取对应校花的名字
    实现方式：
        方式1：
            将所有的url添加到start_urls 列表里面
        方式2：
            手动的添加
            yield scrapy.Request(url=new_url, callback=self.parse)
基于scrapy的五大核心组件
    Spider：
        1.产生url
        2.进行请求发送
        3.数据解析
    引擎
        Spider封装的请求对象会给到引擎
    调度器：
        引擎在把请求对象给调度器
        过滤器：给请求对象进行去重
        队列：放置去重之后的请求对象
    引擎：
        接收数据
        处理事务
        调度器处理完成请求对象之后再给到引擎
    下载器：
        引擎再把请求对象给到下载器
    互联网：
        下载器发送请求给互联网，然后返回一个响应经过下载器和引擎到达Spider
    管道：
        Spider封装item通过引擎给到管道，管道进行持久化存储

请求传参：
    使用场景：
        如果我们要爬取解析的数据不在同一张页面中。(深度爬取)
    需求：
        爬取boss直聘的岗位名称和岗位描述
    使用方法
        scrapy.Request(url=detail_url, callback=self.parse_detail, meta={'item':item})
        通过meta方法进行请求传参
        item = response.meta['item']
        通过response来获取上一个传递过来的参数
图片爬取之ImagePipeline管道类
    基于scrapy爬取字符串类型的数据和爬取图片类型的数据区别
    -字符串：只需要基于xpath进行数据解析提交管道进行持久化存储
    -图片：xpath解析出图片的src属性值，单独的再对图片发起一次请求获取图片二进制类型的数据，比较繁琐
    用ImagePipeline,只需要解析出图片地址就可以
    只需要将img的src属性值进行接卸，提交到管道，管道就会对src进行请求发送获取图片的二进制数据
    需求：爬取站长素材中的高清图片
    使用流程：
        什么是图片的软加载
        1.进行数据解析(图片的地址)
        2.将图片地址提交到指定的管道类(ImagePipeline)
        3.管道类接收处理：
            要重写父类的三个方法
            get_media_request:根据图片地址进行图片数据的请求
            file_path:指定图片进行持久化存储的路径
            item_completed: 返回下一个即将被执行的管道类
        4.在配置文件中：
            指定文件存储的路径
            开启对应的管道类

scrapy框架的中间件：
    下载中间件：在引擎和下载器之间的中间件
        批量的处理整个工程中所有的请求和响应
        1.拦截请求
            -进行ua伪装：为特定的请求进行ua伪装
                一般用process_request来进行ua伪装
            -代理ip的设定：为特定的请求进行代理ip的设定
                一般用process_exceptions来进行代理ip的设定
        2.拦截响应
            -篡改响应数据或者响应对象：来获得动态加载的数据
    爬虫中间件：在引擎和Spider之间的中间件
"""