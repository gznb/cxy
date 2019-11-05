# -*- coding: utf-8 -*-
import scrapy
import time
from cxy.items import CxyItem
import copy


class CxyOneSpider(scrapy.Spider):
    name = 'cxy_one'
    start = time.clock()
    start_urls = ['http://www.qingshu.so/bbqs.html']
    base_url = 'http://www.qingshu.so/'

    def parse(self, response):
        res = response.xpath('//div[@class="item"]')
        for r in res:
            item = CxyItem()
            item['Ctitle'] = ''
            item['Curl'] = self.base_url + r.xpath('./div[@class="info clearfix"]//a/@href').extract_first()
            item['ClikeCounts'] = r.xpath('./div[@class="info clearfix"]//span[@class="xh"]/text()').extract_first()
            item['ClookCounts'] = r.xpath('./div[@class="info clearfix"]//span[@class="pl"]/text()').extract_first()
            item['Ctime'] = r.xpath('./div[@class="info clearfix"]//span[@class="date"]/text()').extract_first()
            item['Ctext'] = ''
            yield scrapy.Request(url=item['Curl'], callback=self.parse_item, meta={'item': copy.deepcopy(item)})

        next_url = response.xpath('//a[contains(text(), "下一页")]/@href').extract_first()
        if next_url is not None:
            # print(next_url)
            yield scrapy.Request(url=self.base_url + next_url)

    def parse_item(self, response):
        item = response.meta['item']
        item['Ctitle'] = response.xpath('//h1[@class="a_title"]/a/text()').extract_first()

        item['Ctext'] = response.xpath("string(//div[@class='a_content clearfix'])").extract_first()

        elapsed = (time.clock() - self.start)  # 显示运行时间
        print("Time used: {}\r".format(elapsed), end="")

        yield item
