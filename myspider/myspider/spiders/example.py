# -*- coding: utf-8 -*-
import scrapy


class ExampleSpider(scrapy.Spider):
    name = 'example' #爬虫名
    allowed_domains = ['example.com']
    start_urls = ['http://baidu.com']

    def parse(self, response):
        #处理start_urls地址对应的响应
        ret1 = response.xpath("//div[@class = ']//h3/text()") 
        print(ret1)