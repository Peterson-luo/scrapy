# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
class MyspyderPipeline(object):
    def process_item(self, item, spider):
        return item
class fenghuangPipeline(object):
    def __init__(self):
        self.f=open('fenghuang.json',"wb")
    def process_item(self, item, spider):
        cont=json.dumps(dict(item),ensure_ascii=False)+'\n'
        self.f.write(cont.encode("utf-8"))
    def close_spider(self,spider):
        self.f.close()

class tencetnPipeline(object):
    def __init__(self):
        self.f=open('tencent_position.json',"wb")
    def process_item(self, item, spider):
        cont=json.dumps(dict(item),ensure_ascii=False)+'\n'
        self.f.write(cont.encode("utf-8"))
        return item
    def close_spider(self,spider):
        self.f.close()

import scrapy,os
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy.utils.project import get_project_settings


class baiduImgPipeline(ImagesPipeline):
    # 获取自己设置的路径
    IMAGES_STORE = get_project_settings().get("IMAGES_STORE")
    def get_media_requests(self, item, info):
        image_url = item['img_url']
        yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        print(image_paths)
        # os.rename(self.IMAGES_STORE+'\\'+image_paths[0].replace('/','\\'),self.IMAGES_STORE+item['img_title'])
        item['image_path'] = self.IMAGES_STORE+'\\'+item['img_title'] #如果不重命名的话，这里设置的是rename的第一个参数