# -*- coding: utf-8 -*-
import scrapy
from ityouknow.items import ItyouknowItem


class ItSpider(scrapy.Spider):
    name = 'it'
    allowed_domains = ['ityouknow.com']
    start_urls = [
        'http://www.ityouknow.com/springboot/2016/03/06/springboot(三)-Spring-Boot中Redis的使用.html']

    def parse(self, response):
        ityouknow = ItyouknowItem()
        for it in response.xpath('//div[@class="col-md-9 markdown-body"]/pre'):
            ityouknow['code'] = it.xpath('.//code/text()').extract()
            print("lililifaf"+ "\n")
            yield ityouknow
