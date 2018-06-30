import scrapy
from mySpyder.items import DmozItem

class fenghuang(scrapy.Spider):
    name = "fenghuang"
    allowed_domains=["ifeng.com"]
    start_urls=["http://culture.ifeng.com/"]

    def parse(self, response):
        news=response.xpath("//div[@class='wenxue']")
        t1=news.xpath(".//div[@class='zxbd']")
        t2=news.xpath(".//div[@class='zxbd_02']")
        items = []
        for each in t1:
            item=DmozItem()
            news_title=each.xpath("./h2/a/text()").extract()
            news_cont=each.xpath("./div[@class='clearfix']/p/a/text()").extract()
            url=each.xpath("./h2/a/@href").extract()
            item["news_title"] = news_title[0]
            item["news_cont"] = news_cont[0]
            item["url"] = url[0]
            items.append(item)
            yield item
        for each in t2:
            item = DmozItem()
            news_title = each.xpath("./h2/a/text()").extract()
            news_cont = each.xpath("./p/a/text()").extract()
            url = each.xpath("./h2/a/@href").extract()
            item["news_title"] = news_title[0]
            item["news_cont"] = news_cont[0]
            item["url"] = url[0]
            yield item
            items.append(item)
        # return items