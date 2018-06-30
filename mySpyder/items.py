# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DmozItem(scrapy.Item):
    name = scrapy.Field()
    cont = scrapy.Field()
    title = scrapy.Field()
    news_title=scrapy.Field()
    news_cont =scrapy.Field()
    url=scrapy.Field()

    position = scrapy.Field()
    position_type = scrapy.Field()
    number = scrapy.Field()
    location = scrapy.Field()
    time = scrapy.Field()
    url = scrapy.Field()


    img_url=scrapy.Field()
    img_title = scrapy.Field()
    image_path=scrapy.Field()#设置图片本地保存链接
