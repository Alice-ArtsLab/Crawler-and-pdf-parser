import scrapy
from scrapy.loader import ItemLoader
from spider.items import SpiderItem

class hodie(scrapy.Spider):
    name = 'hodie'
    start_urls = ["https://www.revistas.ufg.br/musica/issue/archive/1",
                "https://www.revistas.ufg.br/musica/issue/archive/2",
                "https://www.revistas.ufg.br/musica/issue/archive/3",
                "https://www.revistas.ufg.br/musica/issue/archive/4",
                "https://www.revistas.ufg.br/musica/issue/archive/5",
                "https://www.revistas.ufg.br/musica/issue/archive/6",
                "https://www.revistas.ufg.br/musica/issue/archive/7",
                "https://www.revistas.ufg.br/musica/issue/archive/8"]

    def parse(self, response):
        for link in response.xpath('//a[contains(@class,"tit")]/@href').extract():
            yield scrapy.Request(link,meta={'dont_redirect': True}, callback=self.parse2)

    def parse2(self, response):
        for link in response.xpath('//a[contains(@class,"obj")]/@href').extract():
            yield scrapy.Request(link,meta={'dont_redirect': True}, callback=self.parse3)

    def parse3(self, response):
        dl = response.xpath('//a[contains(@class,"download")]/@href').extract()
        loader = ItemLoader(item=SpiderItem(), selector=dl)
        loader.add_value('file_urls', dl)
        yield loader.load_item()

