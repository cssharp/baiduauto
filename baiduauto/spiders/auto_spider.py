#!/usr/bin/env 
#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import scrapy
from baiduauto.items import AutoItem
import urlparse

class AutoSpider(scrapy.spiders.Spider):
	name = "auto"
	allowed_domains = ["baidu.com"]
	start_urls = [
        "http://auto.baidu.com/"
	]
	
	def parse(self,response):
		for sel in response.xpath("//ul/li"):
			item = AutoItem()
			item["title"] = sel.xpath("a/text()").extract()

			urlList = sel.xpath("a/@href").extract()
			newUrlList = []
			for url in urlList:
				newUrlList.append(urlparse.urljoin(response.url,url))

			item["link"] = newUrlList
			item["desc"] = sel.xpath("text()").extract()
			yield item
		