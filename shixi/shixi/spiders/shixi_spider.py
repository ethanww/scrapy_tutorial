#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scrapy.spider import Spider
from scrapy import Request,FormRequest
from shixi.items import ShixiItem

class ShixiSpider(Spider):
    name = 'shixi'
    headers = {
         'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }
    # allowed_domains = ["newsmth.net"]  # 水木清华

    # cookies={
    #     'left-show':'0',
    #     'main[XWJOKE]':'hoho',
    #     'left-index':'00000100000',
    #     'Hm_lvt_9c7f4d9b7c00cb5aba2c637c64a41567':'1493100709|1493624270|1494404344',
    #     'Hm_lpvt_9c7f4d9b7c00cb5aba2c637c64a41567':'1494411554',
    #     'main[UTMPUSERID]':'ethanww',
    #     'main[UTMPKEY]':'69199193',
    #     'main[UTMPNUM]':'8753',
    #     'main[PASSWORD]':'TsrjVL%2506O%25044r%2522%2505f%255C%25193%2503%2502V%2525p%250D%255E'
    # }

    def start_requests(self):
        url = 'http://www.newsmth.net/'  # 水木清华实习信息页面
        # yield Request(url,headers=self.headers)
        # formdata={
        #     'id':'ethanww',
        #     'passwd':'wangyusheng',
        #     'mode':0,
        #     'CookieDate':2
        # }
        # yield FormRequest(url,cookies=self.cookies)
        yield FormRequest(url,formdata=formdata)

    def parse(self, response):
        print(response.text)




