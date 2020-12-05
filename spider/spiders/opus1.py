import scrapy
from scrapy.loader import ItemLoader
from spider.items import SpiderItem

class opus1(scrapy.Spider):
    name = 'opus1'
    start_urls = ['http://www.anppom.com.br/revista/index.php/opus/issue/view/49/showToc',
    'http://www.anppom.com.br/revista/index.php/opus/issue/view/48/showToc',
    'http://www.anppom.com.br/revista/index.php/opus/issue/view/47/showToc',
    'http://www.anppom.com.br/revista/index.php/opus/issue/view/46/showToc',
    'http://www.anppom.com.br/revista/index.php/opus/issue/view/45/showToc',
    'http://www.anppom.com.br/revista/index.php/opus/issue/view/43/showToc',
    'http://www.anppom.com.br/revista/index.php/opus/issue/view/42/showToc']

    def parse(self, response):
        for link in response.xpath('//a[contains(@class,"file")]/@href').extract():
            yield scrapy.Request(link,meta={'dont_redirect': True}, callback=self.parse2)

    def parse2(self, response):
        dl = response.xpath('//a[contains(@class,"action pdf")]/@href').extract()
        loader = ItemLoader(item=SpiderItem(), selector=dl)
        loader.add_value('file_urls', dl)
        yield loader.load_item()

