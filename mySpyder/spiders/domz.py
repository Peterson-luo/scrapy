import scrapy
from mySpyder.items import DmozItem
class dmozSpider(scrapy.Spider):
    #必须定义爬虫名字
    name='dmoz'
    #允许爬取的域名
    allowed_domains=['itcast.cn']
    #要爬取的网站
    start_urls=['http://www.itcast.cn/channel/teacher.shtml#ajavaee']

    #定义处理response方法
    def parse(self, response):

        items = []
        cont=response.xpath("//div[@class='li_txt']")
        for each in cont:
            item = DmozItem()
            name=each.xpath('./h3/text()').extract()
            title = each.xpath("./h4/text()").extract()
            cont = each.xpath("./p/text()").extract()
            item['title'] = title[0]
            item['name'] = name[0]
            item['cont'] = cont[0]
            print(item)
            items.append(item)
        return items
