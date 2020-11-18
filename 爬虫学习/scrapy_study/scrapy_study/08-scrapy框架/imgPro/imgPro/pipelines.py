# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
import scrapy


# class ImgproPipeline:
#     def process_item(self, item, spider):
#         return item

class ImgPipeline(ImagesPipeline):
    """
    要重写父类的三个方法
    get_media_request:根据图片地址进行图片数据的请求
    file_path:指定图片进行持久化存储的路径
    item_completed: 返回下一个即将被执行的管道类
    """

    def get_media_requests(self, item, info):
        yield scrapy.Request(item['img_url'])

    def file_path(self, request, response=None, info=None, *, item=None):
        img_name = request.url.split('/')[-1]
        return img_name

    def item_completed(self, results, item, info):
        return item
