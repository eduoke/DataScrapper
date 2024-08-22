import scrapy


class BrighttalkSpider(scrapy.Spider):
    name = "brighttalk"
    allowed_domains = ["brighttalk.com"]
    start_urls = ["https://brighttalk.com"]

    def parse(self, response):
        pass
