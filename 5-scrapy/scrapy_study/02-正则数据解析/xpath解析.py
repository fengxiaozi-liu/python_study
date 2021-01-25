"""
xpath解析：
    最常用且最便捷高效的一种解析方式，通用性最强的一种解析方式

xpath解析原理：
    实现一个etree的对象，且需要将被解析的页面源码数据加载到该对象中
    调用etree对象中的xpath方法结合着xpath表达式实现标签的定位和内容的捕获
如何实例化etree对象
    将本地的HTML文档中的源码数据加载到etree对象中
        etree.parse(filepath)
    可以将互联网上数据的源码数据加载到该对象中
        etree.HTML('page_text')
xpath表达式：
    /html/head/title /表示从根节点开始定位，一个/表示一个层级
    /html//title 表示的是多个层级，//表示可以从任意的位置去寻找符合条件的标签
    属性定位：
    //div[@class="song"]：定位到class为song的div标签
    索引定位：
    //div[@class="song"]/p[3] 定位到div标签里面的第三个p标签
    取文本：
        /text() 取出直系文本
        //div[@class="tang"]/ul/li[5]/a/text()
        //text() 取出标签下所有的文本内容
    取属性：
        /@属性名
        //div[@class="song"]/img/@src
"""
from lxml import etree

parser = etree.HTMLParser(encoding='utf-8')
tree = etree.parse('../爬虫数据/武沛齐.html', parser=parser)
title = tree.xpath('/html/body/div')
print(title)
