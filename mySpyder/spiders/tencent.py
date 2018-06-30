import scrapy
from mySpyder.items import DmozItem

class tencentSpider(scrapy.Spider):
    name = "tencent"
    allowed_domains=["tencent.com"]
    offset=0
    url="https://hr.tencent.com/position.php?&start="
    start_urls = [url+str(offset)]
    def parse(self, response):
        cont=response.xpath("//tr[@class='even'] | //tr[@class='odd']")
        for each in cont:
            item=DmozItem()
            position=each.xpath("./td[@class='l square']/a/text()").extract()
            position_type =each.xpath("./td[2]/text()").extract()
            number=each.xpath("./td[3]/text()").extract()
            location= each.xpath("./td[4]/text()").extract()
            time = each.xpath("./td[5]/text()").extract()
            url=each.xpath("./td[@class='l square']/a/@href").extract()
            item['position']=position[0]
            item["position_type"]=position_type[0]
            item['number']=number[0]
            item['location']=location[0]
            item['time']=time[0]
            item['url'] = url[0]
            yield item
        if self.offset < 3950:
            self.offset +=10
        yield scrapy.Request(self.url+str(self.offset),callback=self.parse)

