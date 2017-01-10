# -*- coding: utf-8 -*-

from coolscrapy.items import DouBanItem
import scrapy

class  DouBanSpider(scrapy.Spider):

    name = "douban"
    allow_domains=["movie.douban.com"]
    start_urls = ["https://movie.douban.com/explore#!type=movie"]

    def parse(self, response):
        for mov in response.xpath("//div[@class='list']"):
            item = DouBanItem()
            item["title"] = mov.xpath('a/div/img[@alt]').extract()
            item["link"] = mov.xpath('a[@href]').extract()
            item["score"] = mov.xpath('a/p/strong/text()').extract()
            print(item['title'], item['link'], item['desc'])
        return item