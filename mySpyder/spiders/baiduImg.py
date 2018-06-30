import scrapy,json
from mySpyder.items import DmozItem

class baiduImg(scrapy.Spider):
    name = "baiduImg"
    allowed_domain=["baidu.com"]
    key_word='美女'
    page=30
    url='https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%s&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word=%s&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&pn=%s&rn=30&gsm=3c&1522746996904='%(key_word,key_word,page)
    start_urls=[url]
    def parse(self, response):
        item=DmozItem()
        # with open('baiduimg.json','w') as f:
        #     cont=json.dumps(response.body_as_unicode(),ensure_ascii=True)
        #     f.write(cont)
        res=response.body.decode()
        docs=json.loads(res,encoding='utf-8')
        print(docs)
        # docs=json.loads('baiduimg.json',)
        data=docs['data']
        for i in range(0, len(data)):
            urls = data[i]['thumbURL']
            title=str(i+1)+'.jpg'
            item["img_url"]=urls
            item['img_title']=title
            yield item
        if self.page < 300:
            self.page +=30
        url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%s&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word=%s&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&pn=%s&rn=30&gsm=3c&1522746996904=' % (
        self.key_word, self.key_word, self.page)
        yield scrapy.Request(url,callback=self.parse)

