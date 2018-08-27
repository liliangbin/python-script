# -*- coding: utf-8 -*-
import scrapy
from one.items import OneItem


class OnenameSpider(scrapy.Spider):
    name = 'onename'
    allowed_domains = ['m.wufazhuce.com']
    start_urls = ['http://m.wufazhuce.com/one/211']

    def parse(self, response):
        item = OneItem()

        item["imgUrl"] = response.xpath("//*[@id='myPage_angOne_view']/div[4]/div[1]/img/@src").extract()
        item["text"] = response.xpath("//*[@id='myPage_angOne_view']/div[4]/div[1]/p[4]/text()").extract()
        item["day"] = response.xpath("//*[@id='myPage_angOne_view']/div[4]/div[1]/p[2]/text()").extract()
        item["month"] = response.xpath("//*[@id='myPage_angOne_view']/div[4]/div[1]/p[3]/text()").extract()

        yield item

        for i in range(2170, 2178):
            url = "http://m.wufazhuce.com/one/%d" % (i)
            print(url + "\n")
            yield scrapy.Request(url, callback=self.parse)
