# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FbsproItem(scrapy.Item):
    news_kind = scrapy.Field()
    news_title = scrapy.Field()


class DetailItem(scrapy.Item):
    news_content = scrapy.Field()
