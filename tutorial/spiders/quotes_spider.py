# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 17:58:16 2017

@author: Mac
"""
#scrapy crawl quotes 转到爬虫的文件夹后在cmd运行爬虫


import os
import scrapy
import re
from scrapy import Selector

SAVE_HTML=True

class QuotesSpider(scrapy.Spider):
    name = "quotes"  #define the name of this Spider
    start_urls = []
    
    if os.path.exists('quotes.json'):
        os.remove('quotes.json')
    
    #webpage you want to cralw
    url_former = 'https://twitter.com/xx/status/'
    data = [936415082782822401]

    for url in data:       
        start_urls.append(url_former + str(url))


    def parse(self, response):
        
        if SAVE_HTML:
            page = response.url.split("/")[-3]
            filename = 'Twitter-%s.html' % page
            with open(filename, 'wb') as f:
                f.write(response.body)
 
        selector=Selector(response)  
        id = response.url.split("/")[-1]
        #for quote in response.css('div.js-tweet-text-container p::text')[1:]:
        for quote in selector.xpath('//p[@class = "TweetTextSize  js-tweet-text tweet-text"]'):
            yield {
                id:quote.xpath('string(.)').extract()[0]    
            }
                
        #turn to next page    
        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)