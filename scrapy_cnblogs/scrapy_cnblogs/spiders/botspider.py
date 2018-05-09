# -*- coding:UTF-8 -*-


from scrapy.spiders import Spider, Rule
from scrapy.selector import Selector
from scrapy_cnblogs.items import ScrapyCnblogsItem
from scrapy.linkextractors import LinkExtractor
import re
from scrapy.spiders import CrawlSpider


class botspider(CrawlSpider):
    name = 'cnblogSpider'
    allow_domains = ['cnblogs.com']
    start_urls = [

        "http://www.cnblogs.com/fengzheng/default.html?page=3",
    ]

    # rules = (
    #     Rule(LinkExtractor(allow=('fengzheng/default.html\?page\=([\d]+)',), ), callback='parse_item', follow=True)
    # )

    def parse(self, response):
        sel = response.selector
        posts = sel.xpath('//div[@id="mainContent"]/div/div[@class="day"]')
        items = []
        for p in posts:
            # content = p.extract()
            # self.file.write(content.encode("utf-8"))
            item = ScrapyCnblogsItem()
            publishDate = p.xpath('div[@class="dayTitle"]/a/text()').extract_first()

            item["publishDate"] = (publishDate is not None and [publishDate.encode("utf-8")] or [""])[0]
            # self.file.write(title.encode("utf-8"))
            title = p.xpath('div[@class="postTitle"]/a/text()').extract_first()
            print("title = " + title)

            item["title"] = (title is not None and [title.encode("utf-8")] or [""])[0]

            readcount = p.xpath('div[@class="postDesc"]/text()').re_first(u"阅读\(\d+\)")

            regReadCount = re.search(r"\d+", readcount)
            if regReadCount is not None:
                readcount = regReadCount.group()
            item["readCount"] = (readcount is not None and [readcount.encode("utf-8")] or [0])[0]

            commentcount = p.xpath('div[@class="postDesc"]/text()').re_first(u"评论\(\d+\)")
            regCommentCount = re.search(r"\d+", commentcount)
            if regCommentCount is not None:
                commentcount = regCommentCount.group()
            item["commentCount"] = (commentcount is not None and [commentcount.encode("utf-8")] or [0])[0]
            items.append(item)

        return items
